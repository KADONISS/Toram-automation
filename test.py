
import pyautogui as pag
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import pyscreeze

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
def scroll_down(n):
    while (True):
        pyautogui.scroll(-200)
        n -=1
        print(n)
        if(n <=1):
            break
        time.sleep(2)
def get_five_percent(o_data):
	percent = int((o_data/100)*5)
	return percent

        
def CB_receive():
    scroll_down(30)
    while (True):
        time.sleep(1)
        image_location = pyautogui.locateOnScreen('img/image.png', confidence=0.7)
        
        count += 1  # Tăng count khi tìm thấy ảnh
        print(count)
        pyautogui.click(image_location)
        time.sleep(0.8)
        select_item = pyautogui.locateCenterOnScreen('img/select-item.png', confidence=0.9)
        pyautogui.click(select_item)
        time.sleep(0.8)
        
        pyautogui.click(x=1330, y=215, clicks=2, interval=0.25)
        time.sleep(0.8)
        set_price = pyautogui.locateCenterOnScreen('img/Price.png', confidence=0.9)
        pyautogui.click(set_price)
        time.sleep(0.8)
        pyautogui.click(x=1282, y=313)
        pyautogui.press('backspace', presses=3)
        pyautogui.write('21111', interval=0.25)
        pyautogui.press('enter')
        time.sleep(0.8)
        pyautogui.click(x=1234, y=611)
        time.sleep(0.8)
        pyautogui.click(x=1635, y=192)
        time.sleep(0.8)
        Ok_btn = pyautogui.locateCenterOnScreen('img/Ok-btn.png', confidence=0.9)
        pyautogui.click(Ok_btn)
        
pag.FAILSAFE = False
def randomClick(box):
	x_click = int(random.uniform(box.left + get_five_percent(box.left), box.left + box.width - get_five_percent(box.width)))
	y_click = int(random.uniform(box.top + get_five_percent(box.left), box.top+box.height - get_five_percent(box.width)))
	return (x_click, y_click)
def random_time(low,high):
	time = np.random.uniform(low,high)
	return time
def find_image_and_random_click(img_path,fun_name):
	box = pag.locateOnScreen(img_path, grayscale=True, confidence=0.7)
	if box != None:
		print("image found")
		pag.moveTo(randomClick(box),duration = random_time(0.4,0.7))
		pag.mouseDown()
		time.sleep(random_time(0.2,0.5))
		pag.mouseUp() 

def find_image(img_path):
	box = pyscreeze.locateOnScreen(img_path, grayscale=True, confidence=0.7)
	if box != None:
		return True
        
	else:
		return False    


def proc():

    #pag.click(x=1130,y=300, interval=0.75)
    #time.sleep(0.5)
    #1-5
    pag.moveTo(x=1330, y=220, duration=0.1)
    pag.click(x=1330, y=220, clicks= 1, )
    time.sleep(0.2)

    pag.moveTo(x=1430, y=220, duration=0.1)
    pag.click(x=1430, y=220,clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1530, y=220, duration=0.1)
    pag.click(x=1530, y=220, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1670, y=220, duration=0.1)
    pag.click(x=1670, y=220, clicks= 1)
    time.sleep(0.2)


    pag.moveTo(x=1770, y=220, duration=0.1)
    pag.click(x=1770, y=220, clicks= 1)
    time.sleep(0.2)

    #6-10
    pag.moveTo(x=1330, y=330, duration=0.1)
    pag.click(x=1330, y=330, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1430, y=330, duration=0.1)
    pag.click(x=1430, y=330, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1530, y=330, duration=0.1)
    pag.click(x=1530, y=330, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1650, y=330, duration=0.1)
    pag.click(x=1650, y=330, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1800, y=330, duration=0.1)
    pag.click(x=1800, y=330, clicks= 1)
    time.sleep(0.2)
    #11-15

    pag.moveTo(x=1330, y=440, duration=0.1)
    pag.click(x=1330, y=440, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1430, y=440, duration=0.1)
    pag.click(x=1430, y=440, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1530, y=440, duration=0.1)
    pag.click(x=1530, y=440, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1650, y=440, duration=0.1)
    pag.click(x=1650, y=440, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1800, y=440, duration=0.1)
    pag.click(x=1800, y=440, clicks= 1)
    time.sleep(0.2)

    #16-20
    pag.moveTo(x=1330, y=550, duration=0.1)
    pag.click(x=1330, y=550, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1430, y=550, duration=0.1)
    pag.click(x=1430, y=550, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1530, y=550, duration=0.1)
    pag.click(x=1530, y=550, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1650, y=550, duration=0.1)
    pag.click(x=1650, y=550, clicks= 1)
    time.sleep(0.2)

    pag.moveTo(x=1800, y=550, duration=0.1)
    pag.click(x=1800, y=550, clicks= 1)
    time.sleep(0.2)

    pag.click(x=930,y=300, interval=0.75)

    pag.moveTo(x= 1265,y = 624, duration=0.25)
    pag.click(x=1265,y=624, interval=0.75)

    pag.moveTo(x= 1246,y = 603, duration=0.25)
    pag.click(x=1246,y=603, interval=0.75)
#for n in range(2):
#          #check 2s - max create
#          find_image('test.png')
#          pag.click()
#          
#
#          proc()
#          n+= 1
#          print(n)
#          if n == 2:
#                break

find_image_and_random_click('test.png', "2s")
