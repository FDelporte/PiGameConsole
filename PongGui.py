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
    
    speedIncrease = 1
    wasOverlapping = False
    
    stopGame = False
    
    WIDTH = 0
    HEIGHT = 0
    
    PLAYER_OFFSET = 10
    PLAYER_WIDTH = 20
    PLAYER_HEIGHT = 100

    PADDLE_MOVEMENT = 25
    REFRESH_TIME = 5 # milliseconds
    INCREASE_SPEED = 1.0005
    
    countdown = 0
    
    def __init__(self, parent, w, h):
        
        try:
            
            tk.Frame.__init__(self, parent)
            
            # Window dimensions and other constants
            self.WIDTH = w
            self.HEIGHT = h
            
            # Game variables
            self.player1_score = 0
            self.player2_score = 0
            
            # The Tk labels to show the score
            self.player1_score_label = None
            self.player2_score_label = None
            
            # Set up the GUI window via Tk        
            self.canvas = Canvas(self, background="darkblue", width=self.WIDTH, height=self.HEIGHT)
            self.canvas.create_line((self.WIDTH / 2, 0, self.WIDTH / 2, self.HEIGHT), fill="white")
            self.canvas.pack(side="bottom", fill="x", padx=4)
            
            # Keep a reference for the GUI elements
            self.player1 = self.canvas.create_rectangle((self.PLAYER_OFFSET, (self.HEIGHT / 2) - (self.PLAYER_HEIGHT / 2), self.PLAYER_OFFSET + self.PLAYER_WIDTH, (self.HEIGHT / 2) + (self.PLAYER_HEIGHT / 2)), fill="orange")
            self.player2 = self.canvas.create_rectangle((self.WIDTH - (self.PLAYER_OFFSET + self.PLAYER_WIDTH), (self.HEIGHT / 2) - (self.PLAYER_HEIGHT / 2), self.WIDTH - self.PLAYER_OFFSET, (self.HEIGHT / 2) + (self.PLAYER_HEIGHT / 2)), fill="orange")
            self.ball = None  # Set this variable up for reset_ball()
            
            # Ball acceleration (set in reset_ball())
            self.dx = 0
            self.dy = 0
            
            # Prepare the game
            self.reset_ball()
            self.show_scores()
            
            # Countdown
            self.countdown = 5
            
            # Start refresh
            self.refreshJob = self.after(self.REFRESH_TIME, self.refresh)
            
            print "Pong started"

        except:
            
            print "Could not initiate"

    def get(self):
        return self.canvas.get()
    
    def stop(self):
        self.stopGame = True
            
    def move_player(self, playerNumber, direction):    
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

            #self.canvas.update()
        
        except:
            print "move error"
    
    def move_ball(self):    
        self.speedIncrease = self.speedIncrease * self.INCREASE_SPEED
        
        self.canvas.move(self.ball, self.dx * self.speedIncrease, self.dy * self.speedIncrease)    
        
    def show_scores(self):    
        self.canvas.delete(self.player1_score_label)
        self.canvas.delete(self.player2_score_label)
    
        self.player1_score_label = self.canvas.create_text((self.WIDTH / 2) - 60, 40, text=self.player1_score, fill='white', font=('Arial', 30))
        self.player2_score_label = self.canvas.create_text((self.WIDTH / 2) + 50, 40, text=self.player2_score, fill='white', font=('Arial', 30))
        
    def bounce_ball(self):  
        self.dx = -self.dx * self.speedIncrease
        self.dy = random.randint(1, 3) * self.speedIncrease
        self.flip_y = random.randint(0, 1) * 1
    
        if self.flip_y:
            self.dy = -self.dy
        
    def reset_ball(self):    
        self.flip_x = random.randint(0, 1) * 1
        self.dx = random.randint(2, 3)
        self.dy = random.randint(1, 3)
        self.speedIncrease = 1
    
        if self.flip_x == 1:
            self.dx = -self.dx
    
        self.canvas.delete(self.ball)
        self.ball = self.canvas.create_rectangle((self.WIDTH / 4, self.HEIGHT / 4, (self.WIDTH / 4) + 20, (self.HEIGHT / 4) + 20), fill="white")
        
    def show_label(self, player, showText, clearAtEnd):
        placeX = (self.WIDTH / 2) - 300
        
        if player == 2:
            placeX = (self.WIDTH / 2) + 300
        
        for k in range(1, 6):
            goal_label = self.canvas.create_text(placeX, (self.HEIGHT / 2), text=showText, fill='yellow', font=('Arial', 60))
            self.canvas.update()
            
            time.sleep(0.4)
            
            self.canvas.delete(goal_label)
            self.canvas.update()
            
            time.sleep(0.1)
            
        if clearAtEnd == False:
            goal_label = self.canvas.create_text(placeX, (self.HEIGHT / 2), text=showText, fill='yellow', font=('Arial', 60))
        
    def refresh(self):
        if self.countdown > 0:
            
            countdown_label = self.canvas.create_text((self.WIDTH / 2), (self.HEIGHT / 2) - 50, text=str(self.countdown), fill='yellow', font=('Arial', 100))
            self.canvas.update()
            
            time.sleep(1)
            
            self.canvas.delete(countdown_label)
            self.canvas.update()
            
            self.countdown = self.countdown - 1
            
        else:
            self.move_ball()
            
            ball_coords = self.canvas.coords(self.ball)
        
            if ball_coords[0] < 0:
                self.player2_score = self.player2_score + 1
                self.show_scores()
            
                if self.player2_score >= 3:
                    self.show_label(2, "WINNAAR", False)
                    self.stop()
                else:
                    self.show_label(2, "GOAL!!!", True)
                    self.reset_ball()
                
            elif ball_coords[0] > self.WIDTH:
                self.player1_score = self.player1_score + 1
                self.show_scores()
                
                if self.player1_score >= 3:
                    self.show_label(1, "WINNAAR", False)
                    self.stop()
                else:
                    self.show_label(1, "GOAL!!!", True)
                    self.reset_ball()
        
            if ball_coords[1] < 0 or ball_coords[3] > self.HEIGHT:
                self.dy = -self.dy
        
            overlapping = self.canvas.find_overlapping(*ball_coords)
        
            if len(overlapping) > 1:
                collided_item = overlapping[0]
        
                if collided_item == self.player1 or collided_item == self.player2:
                    # To prevent constant wiggling on top of the player box
                    if self.wasOverlapping == False:
                        self.bounce_ball()
                        
                    self.wasOverlapping = True
                else:
                    self.wasOverlapping = False
    
        if self.stopGame == False:
            self.after(self.REFRESH_TIME, self.refresh)
