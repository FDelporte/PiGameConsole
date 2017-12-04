'''
Created on 22/09/2017

@author: Frank Delporte
'''
import thread
import Tkinter as tk
import tkFont
import time

from ButtonHandler import *
from KeyReader import *
from PongGui import *
from SlideShow import *
from ConsoleMenu import *
from Legend import *

try:
    import keyboard # pip install keyboard
    
    keyAvailable = True     
except ImportError:
    keyAvailable = False

class PiGameConsole():
    
    # general vars
    pongBusy = False
    slideShowBusy = False
    keepRunning = False
    
    # frame holders
    menu = None
    legend = None
    win = None
    slideShow = None
    pong = None
        
    def __init__(self):
        print("PiGameConsole initiated")
              
    def preventScreensaver(self):
        
        while (self.keepRunning):
            
            keyboard.write('A', delay=0)
            
            time.sleep(10)
            
    def checkInput(self):
        
        btn = ButtonHandler()
        key = KeyReader()
        
        while (self.keepRunning):    
                    
            if btn.getButton(2) == True or key.getKey("1") == True:
                #print("Controller red")  
                if self.slideShowBusy == True and self.slideShow != None:
                    self.slideShow.stop()
                    self.startPong()
                elif self.pongBusy == True and self.pong != None:
                    self.pong.stop()
                    self.startSlideShow()                    
            
            if btn.getButton(1) == True or key.getKey("2") == True:
                #print("Controller green")  
                print("Controller green")  
            
            if btn.getButton(4) == True or key.getKey("3") == True:
                #print("Player1 red")  
                if self.pongBusy == True and self.pong != None:
                    self.pong.move_player(1, "up")
            
            if btn.getButton(3) == True or key.getKey("4") == True:
                #print("Player1 green")  
                if self.pongBusy == True and self.pong != None:
                    self.pong.move_player(1, "down")
            
            if btn.getButton(6) == True or key.getKey("5") == True:
                #print("Player2 red")  
                if self.pongBusy == True and self.pong != None:
                    self.pong.move_player(2, "up")
            
            if btn.getButton(5) == True or key.getKey("6") == True:
                #print("Player2 green")  
                if self.pongBusy == True and self.pong != None:
                    self.pong.move_player(2, "down")
            
            time.sleep(0.1)
              
    def startGUI(self):
        # Start the GUI
        self.win = tk.Tk()
        self.win.title("PI Gaming console")
        self.win.attributes("-fullscreen", True)
        
        myFont = tkFont.Font(family="Helvetica", size=12, weight="bold")
        
        def exitProgram():
            
            self.keepRunning = False
            print "Finished"
            
            self.win.quit()
            
        self.menu = ConsoleMenu(self.win, 300, 250)
        self.menu.grid(row = 0, column = 0, sticky=tk.NW, padx=(40, 40), pady=(40, 40))
        
        self.legend = Legend(self.win, 300, 400)
        self.legend.grid(row = 1, column = 0, sticky=tk.NW, padx=(40, 40), pady=(40, 40))
        
        self.startSlideShow()
        
        self.win.mainloop()
        
    def clearWindow(self):  
        if self.slideShow != None:
            self.slideShow.stop()            
            self.slideShow = None
            
        if self.pong != None:
            self.pong.stop()            
            self.pong = None
            
        self.slideShowBusy = False
        self.pongBusy = False
        
        time.sleep(0.5)
        
    def startSlideShow(self):          
        self.clearWindow()
        
        self.menu.setSelected(1)
        self.legend.setLegend(1)
        
        self.slideShow = SlideShow(self.win, self.win.winfo_screenwidth() - 300, self.win.winfo_screenheight() - 100)
        self.slideShow.grid(row = 0, column = 2, rowspan = 2, sticky=tk.NSEW, pady=(40, 40))
        
        self.slideShowBusy = True
                
    def startPong(self):        
        self.clearWindow()
        
        self.menu.setSelected(2)
        self.legend.setLegend(2)
        
        self.pong = PongGui(self.win, self.win.winfo_screenwidth() - 300, self.win.winfo_screenheight() - 100)
        self.pong.grid(row = 0, column = 2, rowspan = 2, sticky=tk.NSEW, pady=(40, 40))    
                
        self.pongBusy = True 
    
if __name__ == "__main__":
    
    piGameConsole = PiGameConsole()
        
    # Start a thread to check if a game is running 
    piGameConsole.keepRunning = True
    thread.start_new_thread(piGameConsole.preventScreensaver, ())
    thread.start_new_thread(piGameConsole.checkInput, ())
    
    piGameConsole.startGUI()
