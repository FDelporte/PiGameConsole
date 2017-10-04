'''
Created on 22/09/2017

@author: Frank Delporte
'''

import thread
import Tkinter as tk
import tkFont
import time

from PongGui import *
from msvcrt import getch

class PiGameConsole():
    
    consoleRunning = True
    gameBusy = False
    keepRunning = False
    
    def __init__(self):
        print("PiGameConsole initiated")

    def checkRunning(self):
        
        while (self.keepRunning):
            # if no game is busy start advertisements
            
            # check https://www.daniweb.com/programming/software-development/code/468841/tkinter-image-slide-show-python
            
            time.sleep(1)
            
    def keyboardInput(self):
        
        while (piGameConsole.consoleRunning):
            # Keyboard handler for testing
            cmd = raw_input("Test commands (black/red): Controlbox 1/2 - Player1 3/4 - Player2 5/6")
            
            if cmd == "1":
              print("Controlbox black")  
            elif cmd == "2":
              print("Controlbox red")  
            elif cmd == "3":
              print("Player1 black")  
            elif cmd == "4":
              print("Player1 red")  
            elif cmd == "5":
              print("Player2 black")  
            elif cmd == "6":
              print("Player2 red")  
              
    def startGUI(self):
        # Start the GUI
        win = tk.Tk()
        win.title("PI Gaming console")
        win.attributes("-fullscreen", True)
        
        myFont = tkFont.Font(family="Helvetica", size=12, weight="bold")
        
        def exitProgram():
            consoleRunning = False
            print "Finished"
            win.quit()
        
        exitButton = tk.Button(win, text="Quit", font=myFont, command=exitProgram, bg="grey", height=1, width=24)
        exitButton.grid(row = 0, sticky=tk.NSEW)
        
        #PongGui(win, 300, 200)
        
        tk.mainloop()
    
if __name__ == "__main__":
    
    piGameConsole = PiGameConsole()
        
    # Start a thread to check if a game is running 
    piGameConsole.keepRunning = True
    thread.start_new_thread(piGameConsole.checkRunning, ())
    thread.start_new_thread(piGameConsole.keyboardInput, ())
    
    piGameConsole.startGUI()