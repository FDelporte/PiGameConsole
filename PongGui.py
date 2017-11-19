# Based on code from https://github.com/mattalexpugh/python-games/blob/master/pong-gui.py
# Made by Matt Pugh, distributed as GPLv2
# This code has been modified

# https://stackoverflow.com/questions/16115378/tkinter-example-code-for-multiple-windows-why-wont-buttons-load-correctly

import Tkinter as tk
import random
import time

from Tkinter import *

class PongGui(tk.Frame):
    
    canvas = None
    ball = None
    dx = 30
    dy = 30
    flip_y = 0
    player1 = None
    player1_score = 0
    player1_score_label = ""
    player2 = ""
    player2_score = 0
    player2_score_label = ""
    WIDTH = 0
    HEIGHT = 0
    
    PLAYER_OFFSET = 10
    PLAYER_WIDTH = 20
    PLAYER_HEIGHT = 1
    
    def __init__(self, parent, w, h):
        tk.Frame.__init__(self, parent)
        
        # Window dimensions and other constants
        self.WIDTH = w
        self.HEIGHT = h
        self.PADDLE_MOVEMENT = 5
        self.REFRESH_TIME = 10 # milliseconds
        
        # Game variables
        player1_score = 0
        player2_score = 0
        
        # The Tk labels to show the score
        player1_score_label = None
        player2_score_label = None
        
        # Set up the GUI window via Tk        
        self.canvas = Canvas(self, background="black", width=self.WIDTH, height=self.HEIGHT)
        self.canvas.create_line((self.WIDTH / 2, 0, self.WIDTH / 2, self.HEIGHT), fill="white")
        self.canvas.pack(side="bottom", fill="x", padx=4)
        
        # Keep a reference for the GUI elements
        self.player1 = self.canvas.create_rectangle((self.PLAYER_OFFSET, (self.HEIGHT / 2) - (self.PLAYER_HEIGHT / 2), self.PLAYER_OFFSET + self.PLAYER_WIDTH, (self.HEIGHT / 2) + (self.PLAYER_HEIGHT / 2)), fill="green")
        self.player2 = self.canvas.create_rectangle((self.WIDTH - (self.PLAYER_OFFSET + self.PLAYER_WIDTH), (self.HEIGHT / 2) - (self.PLAYER_HEIGHT / 2), self.WIDTH - self.PLAYER_OFFSET, (self.HEIGHT / 2) + (self.PLAYER_HEIGHT / 2)), fill="green")
        self.ball = None  # Set this variable up for reset_ball()
        
        # Ball acceleration (set in reset_ball())
        self.dx = 0
        self.dy = 0
        
        # Let's play!
        self.reset_ball()
        
        self.after(self.REFRESH_TIME, self.refresh)
        
        print "Pong started"

    def get(self):
        return self.canvas.get()
    
    def move(self, playerNumber, direction):    
        try:
            coords = self.canvas.coords(self.player1)
            
            if playerNumber == 2:
                coords = self.canvas.coords(self.player2)
        
            if (direction == 'up' and coords[1] <= 10) or \
               (direction == 'down' and coords[3] >= self.HEIGHT):
                return False
        
            if direction == 'up':
                movement = -self.PADDLE_MOVEMENT
            else:
                movement = self.PADDLE_MOVEMENT
        
            if playerNumber == 1:
                self.canvas.move(self.player1, 0, movement)
            elif playerNumber == 2:
                self.canvas.move(self.player2, 0, movement)

	    self.canvas.update()
        
        except:
            print "move error"
    
    def move_up(self, event):
        self.move('up')
        
    def move_down(self, event):
        self.move('down')    
    
    def move_ball(self):    
        self.canvas.move(self.ball, self.dx, self.dy)    
    
    def move_player2(self):    
        ball_pos = self.canvas.coords(self.ball)
        comp_pos = self.canvas.coords(self.player2)
    
        '''if ball_pos[1] > comp_pos[1] and comp_pos[3] < self.HEIGHT:
            self.canvas.move(self.player2, 0, self.PADDLE_MOVEMENT)
        elif ball_pos[1] < comp_pos[1] and comp_pos[1] > 10:
            self.canvas.move(self.player2, 0, -self.PADDLE_MOVEMENT)'''
        
    def show_scores(self):    
        self.canvas.delete(self.player1_score_label)
        self.canvas.delete(self.player2_score_label)
    
        self.player1_score_label = self.canvas.create_text((self.WIDTH / 2) - 60, 40, text=self.player1_score, fill='white', font=('Arial', 30))
        self.player2_score_label = self.canvas.create_text((self.WIDTH / 2) + 50, 40, text=self.player2_score, fill='white', font=('Arial', 30))
        
    def bounce_ball(self):  
        self.dx = -self.dx
        self.dy = random.randint(1, 3)
        self.flip_y = random.randint(0, 1) * 1
    
        if self.flip_y:
            self.dy = -self.dy
        
    def reset_ball(self):    
        self.flip_x = random.randint(0, 1) * 1
        self.dx = random.randint(2, 3)
        self.dy = random.randint(1, 3)
    
        if self.flip_x == 1:
            self.dx = -self.dx
    
        self.canvas.delete(self.ball)
        self.ball = self.canvas.create_rectangle((self.WIDTH / 4, self.HEIGHT / 4, (self.WIDTH / 4) + 20, (self.HEIGHT / 4) + 20), fill="white")
        
    def show_goal(self, player):
        placeX = (self.WIDTH / 2) - 300
        
        if player == 2:
            placeX = (self.WIDTH / 2) + 300
        
        for k in range(1, 6):
            goal_label = self.canvas.create_text(placeX, (self.HEIGHT / 2), text="GOAL!!!", fill='green', font=('Arial', 60))
            self.canvas.update()
            
            time.sleep(0.4)
            
            self.canvas.delete(goal_label)
            self.canvas.update()
            
            time.sleep(0.1)
        
    def refresh(self):
        """
        This is the method which updates all elements in the game.
        """    
        self.show_scores()
        self.move_ball()
        self.move_player2()
        ball_coords = self.canvas.coords(self.ball)
    
        if ball_coords[0] < 0:
            self.player2_score = self.player2_score + 1
            self.show_goal(2)
            self.reset_ball()
            
        elif ball_coords[0] > self.WIDTH:
            self.player1_score = self.player1_score + 1
            self.show_goal(1)
            self.reset_ball()
    
        if ball_coords[1] < 0 or ball_coords[3] > self.HEIGHT:
            self.dy = -self.dy
    
        overlapping = self.canvas.find_overlapping(*ball_coords)
    
        if len(overlapping) > 1:
            collided_item = overlapping[0]
    
            if collided_item == self.player1 or collided_item == self.player2:
                self.bounce_ball()
    
        self.master.after(self.REFRESH_TIME, self.refresh)
