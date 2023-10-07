import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return 
    

def collide(data):
    for i in range(400, 600):
        for j in range(608, 715):
            if data[i, j] > 80 and data[i,j] < 180:
                hit('up')
                return 

print("The game will start in 2 seconds")
time.sleep(2)
hit('up')
while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    collide(data)
        
        
