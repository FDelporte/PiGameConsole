import Tkinter as tk

from Tkinter import *

class ConsoleMenu(tk.Frame):
    
    def __init__(self, parent, w, h):
        tk.Frame.__init__(self, parent)
        
        # Set up the GUI window via Tk        
        self.canvas = Canvas(self, width=w, height=h)
        self.canvas.pack(side="bottom", fill="x", padx=4)
        
        Label(self.canvas, text="Menu", font=('', 20)).grid(row = 0, column = 0, columnspan = 2, sticky=tk.W)
        
        self.labelIndicication1 = StringVar()
        Label(self.canvas, textvariable=self.labelIndicication1, font=('', 18), fg="blue").grid(row = 1, column = 0, sticky=tk.W)
        Label(self.canvas, text="Infokrant", font=('', 18)).grid(row = 1, column = 1, sticky=tk.W)
        
        self.labelIndicication2 = StringVar()
        Label(self.canvas, textvariable=self.labelIndicication2, font=('', 18), fg="blue").grid(row = 2, column = 0, sticky=tk.W)
        Label(self.canvas, text="Pong", font=('', 18)).grid(row = 2, column = 1, sticky=tk.W)
        
    def setSelected(self, item):
        
        if self.labelIndicication1 != None:
            self.labelIndicication1.set("")
            self.labelIndicication2.set("")
            
            if item == 1:
                self.labelIndicication1.set(">>>")
            elif item == 2:
                self.labelIndicication2.set(">>>")