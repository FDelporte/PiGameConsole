import Tkinter as tk

from itertools import cycle
from Tkinter import *

import PIL.Image # pip install pillow
#import PIL.ImageTk

class SlideShow(tk.Frame):
    
    canvas = None
    
    image_files = [
        'E:\\GIT\\PiGameConsole\\test_pictures\\somewhere-in-the-hills-121.jpg',
        'E:\\GIT\\PiGameConsole\\test_pictures\\golden-nature-2336.jpg',
        'E:\\GIT\\PiGameConsole\\test_pictures\\sunset-2165.jpg'
    ]
    
    current_image = 0
    
    def __init__(self, parent, w, h):
        tk.Frame.__init__(self, parent)
        
        # Window dimensions and other constants
        self.WIDTH = w
        self.HEIGHT = h
        
        # Set up the GUI window via Tk        
        self.canvas = Canvas(self, background="black", width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack(side="bottom", fill="x", padx=4)
        
        self.showImage()

    def get(self):
        return self.canvas.get()
    
    def showImage(self):
        '''img = ImageTk.PhotoImage(Image.open(self.image_files[self.current_image]))
        
        self.current_image = self.current_image + 1
        imgLbl = Label(self.canvas, image = img)'''