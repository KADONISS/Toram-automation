import pyautogui as pag
import time
import keyboard
running = False
import threading
def on_press(key):
    global running
    if key == keyboard.Key.f1:
        running ^= True
        if running:
            t = threading.Thread(target=price)
            t.start()

def price():
    while running:
        pag.write('32000')
        
        pag.press('enter')
        time.spagleep(3)
while True: #   
    try:
        if keyboard.is_pressed('q'): #
            print("you pressed q")
    except:
        print("no key")
    currenttime = time.time()
    print (f'the new time is {currenttime}' )
    time.sleep(1)