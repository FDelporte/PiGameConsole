import Tkinter as tk

from Tkinter import *

class Legend(tk.Frame):
    
    canvas = None
    
    def __init__(self, parent, w, h):
        tk.Frame.__init__(self, parent)
        
        # Set up the GUI window via Tk        
        self.canvas = Canvas(self, width=w, height=h)
        self.canvas.pack(side="bottom", fill="x", padx=4)
        
        self.labelTitle = StringVar()
        Label(self.canvas, textvariable=self.labelTitle, font=('', 20)).grid(row = 0, column = 0, columnspan = 2, sticky=tk.W)
        
        Label(self.canvas, text="Controller", font=('', 14)).grid(row = 1, column = 0, columnspan = 2, sticky=tk.W)
        
        self.labelControllerRed = StringVar()
        Label(self.canvas, textvariable=self.labelControllerRed, font=('', 14), fg="red").grid(row = 2, column = 0, sticky=tk.W)
        self.labelControllerRedText = StringVar()
        Label(self.canvas, textvariable=self.labelControllerRedText, font=('', 14)).grid(row = 2, column = 1, sticky=tk.W)
        self.labelControllerGreen = StringVar()
        Label(self.canvas, textvariable=self.labelControllerGreen, font=('', 14), fg="green").grid(row = 3, column = 0, sticky=tk.W)
        self.labelControllerGreenText = StringVar()
        Label(self.canvas, textvariable=self.labelControllerGreenText, font=('', 14)).grid(row = 3, column = 1, sticky=tk.W)
        
        self.labelPlayer1 = StringVar()
        Label(self.canvas, textvariable=self.labelPlayer1, font=('', 14)).grid(row = 4, column = 0, columnspan = 2, sticky=tk.W)
        
        self.labelPlayer1Red = StringVar()
        Label(self.canvas, textvariable=self.labelPlayer1Red, font=('', 14), fg="red").grid(row = 5, column = 0, sticky=tk.W)
        self.labelPlayer1RedText = StringVar()
        Label(self.canvas, textvariable=self.labelPlayer1RedText, font=('', 14)).grid(row = 5, column = 1, sticky=tk.W)
        self.labelPlayer1Green = StringVar()
        Label(self.canvas, textvariable=self.labelPlayer1Green, font=('', 14), fg="green").grid(row = 6, column = 0, sticky=tk.W)
        self.labelPlayer1GreenText = StringVar()
        Label(self.canvas, textvariable=self.labelPlayer1GreenText, font=('', 14)).grid(row = 6, column = 1, sticky=tk.W)
        
        self.labelPlayer2 = StringVar()
        Label(self.canvas, textvariable=self.labelPlayer2, font=('', 14)).grid(row = 7, column = 0, columnspan = 2, sticky=tk.W)
        
        self.labelPlayer2Red = StringVar()
        Label(self.canvas, textvariable=self.labelPlayer2Red, font=('', 14), fg="red").grid(row = 8, column = 0, sticky=tk.W)
        self.labelPlayer2RedText = StringVar()
        Label(self.canvas, textvariable=self.labelPlayer2RedText, font=('', 14)).grid(row = 8, column = 1, sticky=tk.W)
        self.labelPlayer2Green = StringVar()
        Label(self.canvas, textvariable=self.labelPlayer2Green, font=('', 14), fg="green").grid(row = 9, column = 0, sticky=tk.W)
        self.labelPlayer2GreenText = StringVar()
        Label(self.canvas, textvariable=self.labelPlayer2GreenText, font=('', 14)).grid(row = 9, column = 1, sticky=tk.W)

        
    def setLegend(self, menuType):
        
        if self.labelTitle != None:
        
            txtTitle = ""
            txtControllerA = ""
            txtControllerB = ""
            txtPlayer1A = ""
            txtPlayer1B = ""
            txtPlayer2A = ""
            txtPlayer2B = ""
            
            if menuType == 1:
                txtTitle = "Slideshow"
                txtControllerA = "Start Pong"
            
            elif menuType == 2:
                txtTitle = "Pong"
                txtControllerA = "Stop Pong"
                txtPlayer1A = "Op"
                txtPlayer1B = "Neer"
                txtPlayer2A = "Op"
                txtPlayer2B = "Neer"
                
            self.labelTitle.set(txtTitle)
 
            self.labelControllerRed.set(("Rood" if txtControllerA != "" else ""))
            self.labelControllerRedText.set(txtControllerA)
            self.labelControllerGreen.set(("Groen" if txtControllerB != "" else ""))
            self.labelControllerGreenText.set(txtControllerB)
            
            self.labelPlayer1.set(("Speler 1" if txtPlayer1A != "" and txtPlayer1A != "" else ""))
            
            self.labelPlayer1Red.set(("Rood" if txtPlayer1A != "" else ""))
            self.labelPlayer1RedText.set(txtPlayer1A)
            self.labelPlayer1Green.set(("Groen" if txtPlayer1B != "" else ""))
            self.labelPlayer1GreenText.set(txtPlayer1B)
            
            self.labelPlayer2.set(("Speler 2" if txtPlayer2A != "" and txtPlayer2A != "" else ""))
            
            self.labelPlayer2Red.set(("Rood" if txtPlayer2A != "" else ""))
            self.labelPlayer2RedText.set(txtPlayer2A)
            self.labelPlayer2Green.set(("Groen" if txtPlayer2B != "" else ""))
            self.labelPlayer2GreenText.set(txtPlayer2B)
