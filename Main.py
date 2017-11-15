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
#from SlideShow import *

class PiGameConsole():
    
    consoleRunning = True
    pongBusy = False
    keepRunning = False
    
    win = None
    pong = None
        
    def __init__(self):
        print("PiGameConsole initiated")

    def checkRunning(self):
        
        while (self.keepRunning):
            # if no game is busy start advertisements
            
            # check https://www.daniweb.com/programming/software-development/code/468841/tkinter-image-slide-show-python
            
            time.sleep(1)
            
    def checkInput(self):
        
        btn = ButtonHandler()
        key = KeyReader()
        
        while (piGameConsole.consoleRunning):            
            if btn.getButton(1) == True or key.getKey("1") == True:
                print("Controlbox black")  
            
            if btn.getButton(2) == True or key.getKey("2") == True:
                print("Controlbox red")  
            
            if btn.getButton(3) == True or key.getKey("3") == True:
                #print("Player1 black")  
                if self.pongBusy == True and self.pong != None:
                    self.pong.move(1, "up")
            
            if btn.getButton(4) == True or key.getKey("4") == True:
                #print("Player1 red")  
                if self.pongBusy == True and self.pong != None:
                    self.pong.move(1, "down")
            
            if btn.getButton(5) == True or key.getKey("5") == True:
                #print("Player2 black")  
                if self.pongBusy == True and self.pong != None:
                    self.pong.move(2, "up")
            
            if btn.getButton(6) == True or key.getKey("6") == True:
                #print("Player2 red")  
                if self.pongBusy == True and self.pong != None:
                    self.pong.move(2, "down")
            
            time.sleep(0.01)
              
    def startGUI(self):
        # Start the GUI
        self.win = tk.Tk()
        self.win.title("PI Gaming console")
        self.win.attributes("-fullscreen", True)
        
        myFont = tkFont.Font(family="Helvetica", size=12, weight="bold")
        
        def exitProgram():
            consoleRunning = False
            print "Finished"
            self.win.quit()
        
        #exitButton = tk.Button(self.win, text="Quit", font=myFont, command=exitProgram, bg="grey", height=1, width=24)
        #exitButton.grid(row = 0, sticky=tk.NSEW)
        
        self.showButtonControls(1)
        self.showMenu(1)
        
        #self.startSlideShow()
        self.startPong()
        
        self.win.mainloop()
        
    '''def startSlideShow(self):
        slideShow = SlideShow(self.win, 1400, 960)
        slideShow.grid(row = 0, column = 2, rowspan = 2, sticky=tk.NSEW, pady=(40, 40))   '''
        
    def startPong(self):        
        self.pong = PongGui(self.win, 1400, 960)
        self.pong.grid(row = 0, column = 2, rowspan = 2, sticky=tk.NSEW, pady=(40, 40))    
        
        self.pongBusy = True 
                
    def showMenu(self, item):      
        menuFrame = Frame(self.win)
        menuFrame.grid(row = 0, column = 0, sticky=tk.NW, padx=(40, 40), pady=(40, 40))   
        
        Label(menuFrame, text="Menu", font=('', 20)).grid(row = 0, column = 0, columnspan = 2, sticky=tk.W)
        
        Label(menuFrame, text=(">>>" if item == 1 else ""), font=('', 18), fg="blue").grid(row = 1, column = 0, sticky=tk.W)
        Label(menuFrame, text="Infokrant", font=('', 18)).grid(row = 1, column = 1, sticky=tk.W)
        Label(menuFrame, text=(">>>" if item == 2 else ""), font=('', 18), fg="blue").grid(row = 2, column = 0, sticky=tk.W)
        Label(menuFrame, text="Pong", font=('', 18)).grid(row = 2, column = 1, sticky=tk.W)
        
    def showButtonControls(self, type):
        controlFrame = Frame(self.win)
        controlFrame.grid(row = 1, column = 0, sticky=tk.NW, padx=(40, 40), pady=(40, 40))
        
        txtLabel = ""
        txtControllerA = ""
        txtControllerA = ""
        txtPlayer1A = ""
        txtPlayer1B = ""
        txtPlayer2A = ""
        txtPlayer2B = ""
        
        if type == 1:
            txtLabel = "Maak uw keuze"
            txtControllerA = "Spel kiezen"
            txtControllerB = "Starten"
        
        elif type == 2:
            txtLabel = "Pong"
            txtControllerA = "Terug naar hoofdmenu"
            txtControllerB = ""
            txtPlayer1A = "Op"
            txtPlayer1B = "Neer"
            txtPlayer2A = "Op"
            txtPlayer2B = "Neer"
            
        Label(controlFrame, text=txtLabel, font=('', 20)).grid(row = 0, column = 0, columnspan = 2, sticky=tk.W)
        
        Label(controlFrame, text="Controller", font=('', 18)).grid(row = 1, column = 0, columnspan = 2, sticky=tk.W)
        
        Label(controlFrame, text=("Rood" if txtControllerA != "" else ""), font=('', 14), fg="red").grid(row = 2, column = 0, sticky=tk.W)
        Label(controlFrame, text=txtControllerA, font=('', 14)).grid(row = 2, column = 1, sticky=tk.W)
        Label(controlFrame, text=("Groen" if txtControllerB != "" else ""), font=('', 14), fg="green").grid(row = 3, column = 0, sticky=tk.W)
        Label(controlFrame, text=txtControllerB, font=('', 14)).grid(row = 3, column = 1, sticky=tk.W)
        
        Label(controlFrame, text=("Speler 1" if txtPlayer1A != "" and txtPlayer1A != "" else ""), font=('', 14)).grid(row = 4, column = 0, columnspan = 2, sticky=tk.W)
        
        Label(controlFrame, text=("Rood" if txtPlayer1A != "" else ""), font=('', 14), fg="red").grid(row = 5, column = 0, sticky=tk.W)
        Label(controlFrame, text=txtPlayer1A, font=('', 14)).grid(row = 5, column = 1, sticky=tk.W)
        Label(controlFrame, text=("Groen" if txtPlayer1B != "" else ""), font=('', 14), fg="green").grid(row = 6, column = 0, sticky=tk.W)
        Label(controlFrame, text=txtPlayer1B, font=('', 14)).grid(row = 6, column = 1, sticky=tk.W)
        
        Label(controlFrame, text=("Speler 2" if txtPlayer2A != "" and txtPlayer2A != "" else ""), font=('', 14)).grid(row = 7, column = 0, columnspan = 2, sticky=tk.W)
        
        Label(controlFrame, text=("Rood" if txtPlayer2A != "" else ""), font=('', 14), fg="red").grid(row = 8, column = 0, sticky=tk.W)
        Label(controlFrame, text=txtPlayer2A, font=('', 14)).grid(row = 8, column = 1, sticky=tk.W)
        Label(controlFrame, text=("Groen" if txtPlayer2B != "" else ""), font=('', 14), fg="green").grid(row = 9, column = 0, sticky=tk.W)
        Label(controlFrame, text=txtPlayer2B, font=('', 14)).grid(row = 9, column = 1, sticky=tk.W)
    
if __name__ == "__main__":
    
    piGameConsole = PiGameConsole()
        
    # Start a thread to check if a game is running 
    piGameConsole.keepRunning = True
    thread.start_new_thread(piGameConsole.checkRunning, ())
    thread.start_new_thread(piGameConsole.checkInput, ())
    
    piGameConsole.startGUI()