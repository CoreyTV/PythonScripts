from time import sleep
#
import pyautogui
import keyboard
sleep(3)
count=1
right=0
while True:
        if(count%50==0 and right==0):
                pyautogui.moveTo(x=170, y=0)
                right=1
        elif(count%50==0 and right==1):
                pyautogui.moveTo(x=-170, y=0)
                right=0
        sleep(0.26)
        pyautogui.keyDown('j')
        pyautogui.keyUp('j')
        count+=1


# while True:
#         print(pyautogui.position())