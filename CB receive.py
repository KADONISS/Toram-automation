from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import pyscreeze
#pyautogui.displayMousePosition()\
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
pyautogui.displayMousePosition()
def check_and_click_image():
    
    global count  # Sử dụng biến toàn cục count
    
    
    # Kiểm tra xem count đã đạt đến 10 chưa
    if count < 50:
        image_location = pyautogui.locateCenterOnScreen('img/image.png', confidence=0.7)
        
        count += 1  # Tăng count khi tìm thấy ảnh
        print(count)
        pyautogui.click(image_location)
        time.sleep(0.8)
        select_item = pyautogui.locateOnScreen('img/select-item.png', confidence=0.9)
        pyautogui.click(select_item, interval=0.25)
        
        pyautogui.click(x=1550,y= 320, clicks = 1, interval=0.32)
        time.sleep(0.8)
        
        pyautogui.click(x=1330, y=215, clicks=2, interval=0.25)
        time.sleep(0.8)
        set_price = pyautogui.locateCenterOnScreen('img/Price.png', confidence=0.9)
        pyautogui.click(set_price)
        time.sleep(0.8)
        pyautogui.click(x=1282, y=313)
        pyautogui.press('backspace', presses=3)
        pyautogui.write('100000', interval=0.25)
        pyautogui.press('enter')
        time.sleep(0.8)
        pyautogui.click(x=1234, y=611)
        time.sleep(0.8)
        pyautogui.click(x=1635, y=192)
        time.sleep(0.8)
        Ok_btn = pyautogui.locateCenterOnScreen('img/Ok-btn.png', confidence=0.9)
        pyautogui.click(Ok_btn)
        
        
          

   
    
    
def scroll_down(n):
        for i in range(n):
            pyautogui.scroll(-50)
            time.sleep(1)



count = 0
while (True):
    check_and_click_image()
