import pyautogui as pag
import time 
max_create_count = 20
complete = False
time.sleep(0.3)

while not complete:

    pag.click(x=1677, y=221,interval=0.65)
    time.sleep(0.1)

    
    pag.click(x=1264, y=669 , interval=0.65)
    time.sleep(0.1)


    max_create_count = max_create_count -1
    print(max_create_count)

    if(max_create_count <=1):
       break
