from pyautogui import *
import pyautogui as pag
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import pyscreeze
from playsound import playsound
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
#----------------------------Random Time------------------------------#
def random_time(low,high):
	time = np.random.uniform(low,high)
	return time

#----------------------------Random Pixel------------------------------#
def random_pixel_in_button(x,y):
	n1 = np.random.uniform(0,5)
	n2 = np.random.uniform(0,5)
	x = x + n1
	y = y + n2
	return x,y

#----------------------------Random Click on image------------------------------#
def find_image_and_random_click(img_path,fun_name):
	box = pag.locateOnScreen(img_path, grayscale=True, confidence=0.7)
	if box != None:
		print("image found")
		pag.moveTo(randomClick(box),duration = random_time(0.4,0.7))
		pag.click(randomClick(box), duration= 0.4)
		
def find_image_2s(img_path,fun_name):
	box = pag.locateOnScreen(img_path, grayscale=True, confidence=0.9)
	if box != None:
		print("image found")
		pag.moveTo(randomClick(box),duration = random_time(0.4,0.7))
		pag.mouseDown()
		time.sleep(random_time(0.2,0.5))
		pag.mouseUp() 
#----------------------------Random Click Location------------------------------#
def randomClick(box):
	x_click = int(random.uniform(box.left + get_five_percent(box.left), box.left + box.width - get_five_percent(box.width)))
	y_click = int(random.uniform(box.top + get_five_percent(box.left), box.top+box.height - get_five_percent(box.width)))
	return (x_click, y_click)

########## Input/Output ############

#----------------------------Mouse input------------------------------#
def m_click(x,y):
	pag.moveTo(x,y,duration = random_time(0.4,0.7))
	pag.mouseDown()
	time.sleep(random_time(0.2,0.5))
	pag.mouseUp() 

#----------------------------Keyboard input------------------------------#
def key_click(value_k):
	if isinstance(value_k,int):
		value_k = str(value_k)
	pag.keyDown(value_k)
	time.sleep(random_time(0.2,0.5))
	pag.keyUp(value_k)
	time.sleep(random_time(0.3,0.7))

######### Image Processing ###############

#----------------------------Find Image------------------------------#
def find_image(img_path):
	box = pag.locateOnScreen(img_path, grayscale=True, confidence=0.7)
	if box != None:
		return True
	else:
		return False

#----------------------------Check Color------------------------------#
def check_color_at(x,y,color_code,rgb_v):
	if pag.pixel(x,y)[rgb_v] == color_code:
		return True
	else:
		return False

####### Calculations #############

#----------------------------Get 5%------------------------------#
def get_five_percent(o_data):
	percent = int((o_data/100)*5)
	return percent

def craft_ammor(max_create_count):

    


    while (True):
        
        pag.moveTo(x=1443, y=547, duration=0.241)
        pag.click(x=1443, y=547)
        time.sleep(0.4)
        
        pag.moveTo(x=1505, y=210, duration=0.214)
        pag.click(x=1505, y=210)
        time.sleep(0.4)
        
        pag.moveTo(x=895, y=615, duration=0.144)
        pag.click(x=895, y=615)
        time.sleep(0.4)
        
        pag.moveTo(x=1282, y=610, duration=0.148)
        pag.click(x=1282, y=610)
        time.sleep(4.5)
        
        
        pag.moveTo(x=1252, y=603, duration=0.127)
        pag.click(x=1252, y=603)
        time.sleep(1.56)
        

        max_create_count -= 1
        print(max_create_count)
        
        if(max_create_count <=0):
            break

def random_time(low,high):
	time = np.random.uniform(low,high)
	return time

def randomClick(box):
	x_click = int(random.uniform(box.left + get_five_percent(box.left), box.left + box.width - get_five_percent(box.width)))
	y_click = int(random.uniform(box.top + get_five_percent(box.left), box.top+box.height - get_five_percent(box.width)))
	return (x_click, y_click)

def find_image(img_path):
	box = pag.locateOnScreen(img_path, grayscale=True, confidence=0.7)
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
    
max_create_count = 32
count = 2
while (True):
    pag.click(x=1845,y=475 ,interval=0.75)
    time.sleep(1)
    for i in range(8):
        pag.scroll(-50)
    time.sleep(0.75)
    craft_ammor(max_create_count)
    pag.rightClick(x=1200,y=400, interval=0.78)
    time.sleep(1)
    pag.click(x=1295,y=475,interval=0.4)
    time.sleep
    pag.click(x=1120,y=300,interval=0.4)
    for n in range(2):
        #check 2s - max create
        find_image_and_random_click('hahaa.png', "2s")
			
        time.sleep(random_time(1,3))
        proc()
        n+=1
        if n == 2:
              break
    pag.rightClick(x=1200,y=400, interval=0.78)
    
