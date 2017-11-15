'''
Created on Nov 7, 2017

@author: frank
'''    

try:
    import keyboard # pip install keyboard
    
    keyAvailable = True     
except ImportError:
    keyAvailable = False
    
import time

class KeyReader():
    
    def getKey(self, key):
        # Return the key pressed state          
        if keyboard.is_pressed(key) == False:
            return 0  
        else:    
            return 1
        
if __name__ == "__main__":
    
    key = KeyReader()
    
    while (True):
        
        print(str(key.getKey("1")) + "," + str(key.getKey("2")) + "," + str(key.getKey("3")) + "," + str(key.getKey("4")) + "," + str(key.getKey("5")) + "," + str(key.getKey("6")))
        
        time.sleep(0.1)
        
        
        
