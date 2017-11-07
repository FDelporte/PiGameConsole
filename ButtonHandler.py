'''
Created on Nov 7, 2017

@author: frank
'''

import RPi.GPIO as GPIO # pip install RPi.GPIO
import time

class ButtonHandler():
    
    port_controller_green = 19
    port_controller_red = 26
    port_player1_green = 13
    port_player1_red = 06
    port_player2_green = 21
    port_player2_red = 22
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(port_controller_green, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(port_controller_red, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(port_player1_green, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(port_player1_red, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(port_player2_green, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(port_player2_red, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
    def getButton(self, buttonNumber):
        # Return the button state        
        if buttonNumber == 1:
            return GPIO.input(self.port_controller_green);
        elif buttonNumber == 2:
            return GPIO.input(self.port_controller_red);
        elif buttonNumber == 3:
            return GPIO.input(self.port_player1_green);
        elif buttonNumber == 4:
            return GPIO.input(self.port_player1_red);
        elif buttonNumber == 5:
            return GPIO.input(self.port_player2_green);
        elif buttonNumber == 6:
            return GPIO.input(self.port_player2_red);
        
if __name__ == "__main__":
    
    btn = ButtonHandler()
    
    while (True):
        
        print(str(btn.getButton(1)) + "," + str(btn.getButton(2)) + "," + str(btn.getButton(3)) + "," + str(btn.getButton(4)) + "," + str(btn.getButton(5)) + "," + str(btn.getButton(6)))
        
        time.sleep(0.1)
        
        
        