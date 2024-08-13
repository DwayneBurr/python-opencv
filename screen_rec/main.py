import cv2 as cv
import numpy as np
import os
import pyautogui as py

os.chdir(os.path.dirname(os.path.abspath(__file__)))

while(True):
    screenshot = py.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow('Computer vision', screenshot)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done')
