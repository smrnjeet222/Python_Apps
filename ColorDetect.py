import pyautogui


while True: 
    posXY = pyautogui.position() 
    print(posXY, pyautogui.pixel(posXY[0], posXY[1]) )
    if posXY[0] == 0:
        break