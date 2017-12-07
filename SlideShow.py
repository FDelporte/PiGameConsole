import Tkinter as tk

from itertools import cycle
from Tkinter import *
from PIL import Image, ImageTk # pip install pillow + sudo apt-get install python-imaging-tk

# based on example found on 
# https://raspberrypi.stackexchange.com/questions/18261/how-do-i-display-an-image-file-png-in-a-simple-window

class SlideShow(tk.Frame):
    
    canvas = None
    
    current_image = 0
    
    stopShowing = False
    
    SLIDE_DURATION = 7500
    
    def __init__(self, parent, w, h):
        tk.Frame.__init__(self, parent)
        
        # Set up the GUI window via Tk        
        self.canvas = Canvas(self, background="black", width=w, height=h)
        self.canvas.pack(side="bottom", fill="x", padx=4)
        
        # pick an image file you have .bmp  .jpg  .gif.  .png
        # load the file and covert it to a Tkinter image object
        self.image1 = ImageTk.PhotoImage(Image.open('pictures/ouderraad1.jpg'))
        self.image2 = ImageTk.PhotoImage(Image.open('pictures/ouderraad2.jpg'))
        self.image3 = ImageTk.PhotoImage(Image.open('pictures/ouderraad3.jpg'))

        # make the root window the size of the image
        #self.canvas.geometry("%dx%d+%d+%d" % (w, h, 0, 0))

        # root has no image argument, so use a label as a panel
        self.panel1 = tk.Label(self.canvas, image=self.image1)
        self.display = self.image1
        self.panel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        
        print "Display image1"
        
        self.after(self.SLIDE_DURATION, self.update_image)
        #self.root.mainloop()

    def stop(self):
        self.stopShowing = True
        
    def update_image(self):
        if self.display == self.image1:
            self.panel1.configure(image=self.image2)
            print "Display image2"
            self.display = self.image2
        elif self.display == self.image2:
            self.panel1.configure(image=self.image3)
            print "Display image3"
            self.display = self.image3
        else:
            self.panel1.configure(image=self.image1)
            print "Display image1"
            self.display = self.image1
        
        if self.stopShowing == False:
            self.after(self.SLIDE_DURATION, self.update_image)       # Set to call again in 30 seconds