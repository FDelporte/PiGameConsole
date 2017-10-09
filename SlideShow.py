# Based on code from https://www.daniweb.com/programming/software-development/code/468841/tkinter-image-slide-show-python
# Made by https://www.daniweb.com/members/19440/vegaseat
# This code has been modified

import Tkinter as tk

from itertools import cycle
from Tkinter import *

class SlideShow(tk.Frame):
    
    canvas = None
    
    # set milliseconds time between slides
    delay = 3500
    
    # get a series of gif images you have in the working folder
    # or use full path, or set directory to where the images are
    image_files = [
        'Slide_Farm.gif',
        'Slide_House.gif',
        'Slide_Sunset.gif',
        'Slide_Pond.gif',
        'Slide_Python.gif'
    ]
    
    # upper left corner coordinates of app window
    x = 100
    y = 50
    
    def __init__(self, parent, w, h):
        tk.Frame.__init__(self, parent)
        
        # Window dimensions and other constants
        self.WIDTH = w
        self.HEIGHT = h
        
        # Set up the GUI window via Tk        
        self.canvas = Canvas(self, background="black", width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack(side="bottom", fill="x", padx=4)
        
        # set x, y position only
        #self.geometry('+{}+{}'.format(0, 0))
        self.delay = delay
        
        # allows repeat cycling through the pictures
        # store as (img_object, img_name) tuple
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_files)
        self.picture_display = tk.Label(self.canvas)
        self.picture_display.pack()

    def get(self):
        return self.canvas.get()
        
    def show_slides(self):
        '''cycle through the images and show them'''
        # next works with Python26 or higher
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        # shows the image filename, but could be expanded
        # to show an associated description of the image
        self.title(img_name)
        self.after(self.delay, self.show_slides)
