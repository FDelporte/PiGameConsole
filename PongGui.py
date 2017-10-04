# Based on code from https://github.com/mattalexpugh/python-games/blob/master/pong-gui.py
# Made by Matt Pugh, distributed as GPLv2
# This code has been modified

from Tkinter import *
import random

class PongGui(object):
    
    canvas = ""
    ball = ""
    dx = 0 
    dy = 0
    computer = ""
    computer_score = 0
    computer_score_label = ""
    player = ""
    player_score = 0
    player_score_label = ""
    master = Tk()
    PADDLE_MOVEMENT = 0
    REFRESH_TIME = 0
    WIDTH = 0
    HEIGHT = 0

    def move(self, direction):    
        coords = canvas.coords(player)
    
        if (direction == 'up' and coords[1] <= 10) or \
           (direction == 'down' and coords[3] >= HEIGHT):
           return False
    
        if direction == 'up':
            movement = -PADDLE_MOVEMENT
        else:
            movement = PADDLE_MOVEMENT
    
        canvas.move(player, 0, movement)
    
    def move_up(self, event):
        self.move('up')
        
    def move_down(self, event):
        self.move('down')    
    
    def move_ball(self):    
        self.canvas.move(self.ball, self.dx, self.dy)    
    
    def move_computer(self):    
        ball_pos = self.canvas.coords(self.ball)
        comp_pos = self.canvas.coords(self.computer)
    
        '''if ball_pos[1] > comp_pos[1] and comp_pos[3] < self.HEIGHT:
            self.canvas.move(self.computer, 0, self.PADDLE_MOVEMENT)
        elif ball_pos[1] < comp_pos[1] and comp_pos[1] > 10:
            self.canvas.move(self.computer, 0, -self.PADDLE_MOVEMENT)'''
        
    def show_scores(self):    
        self.canvas.delete(self.player_score_label)
        self.canvas.delete(self.computer_score_label)
    
        self.player_score_label = self.canvas.create_text(190, 15, text=self.player_score, fill='white', font=('Arial', 15))
        self.computer_score_label = self.canvas.create_text(210, 15, text=self.computer_score, fill='white', font=('Arial', 15))
        
    def bounce_ball(self):  
        self.dx = -self.dx
        self.dy = random.randint(1, 3)
        flip_y = random.randint(0, 1) * 1
    
        if flip_y:
            self.dy = -self.dy
        
    def reset_ball(self):    
        flip_x = random.randint(0, 1) * 1
        dx = random.randint(2, 3)
        dy = random.randint(1, 3)
    
        if flip_x == 1:
            dx = -dx
    
        self.canvas.delete(self.ball)
        self.ball = self.canvas.create_rectangle((190, 190, 210, 210), fill="white")
        
    def refresh(self):
        """
        This is the method which updates all elements in the game.
        """    
        self.show_scores()
        self.move_ball()
        self.move_computer()
        ball_coords = self.canvas.coords(self.ball)
    
        if ball_coords[0] < 0:
            self.computer_score = self.computer_score + 1
            self.reset_ball()
        elif ball_coords[0] > self.WIDTH:
            self.player_score = self.player_score + 1
            self.reset_ball()
    
        if ball_coords[1] < 0 or ball_coords[3] > self.HEIGHT:
            self.dy = -self.dy
    
        overlapping = self.canvas.find_overlapping(*ball_coords)
    
        if len(overlapping) > 1:
            collided_item = overlapping[0]
    
            if collided_item == self.player or collided_item == self.computer:
                self.bounce_ball()
    
        self.master.after(self.REFRESH_TIME, self.refresh)
    
    def __init__(self, win, w, h):
        # Window dimensions and other constants
        WIDTH = w
        HEIGHT = h
        PADDLE_MOVEMENT = 5
        REFRESH_TIME = 10  # milliseconds
        
        # Game variables
        player_score = 0
        computer_score = 0
        
        # The Tk labels to show the score
        player_score_label = None
        computer_score_label = None
        
        # Set up the GUI window via Tk
        self.master = win
        self.master.title("Pong in Python / Tk!")
        
        self.canvas = Canvas(self.master, background="black", width=self.WIDTH, height=self.HEIGHT)
        self.canvas.create_line((200, 0, 200, 400), fill="white")
        
        # Keep a reference for the GUI elements
        player = self.canvas.create_rectangle((10, 150, 30, 250), fill="white")
        computer = self.canvas.create_rectangle((370, 150, 390, 250), fill="white")
        ball = None  # Set this variable up for reset_ball()
        
        # Ball acceleration (set in reset_ball())
        dx = 0
        dy = 0
        
        self.canvas.pack()
        
        # Bind the keyboard events to our functions
        self.master.bind("<KeyPress-Up>", self.move_up)
        self.master.bind("<KeyPress-Down>", self.move_down)
        
        # Let's play!
        self.reset_ball()
        self.master.after(self.REFRESH_TIME, self.refresh)
        self.master.mainloop()