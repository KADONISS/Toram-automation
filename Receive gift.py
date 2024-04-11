import pyautogui as pag
import time 
max_create_count = 4
complete = False
time.sleep(0.3)

while not complete:
    pag.moveTo(x=1583, y=326, duration=1)
    pag.click(x=1583, y=326)
    time.sleep(0.1)

    pag.moveTo(x=1175, y=985, duration=1)
    pag.click(x=1175, y=985)
    time.sleep(0.1)


    max_create_count = max_create_count -1
    print(max_create_count)

    if(max_create_count <=1):
       break