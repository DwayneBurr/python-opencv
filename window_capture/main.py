import cv2 as cv
import numpy as np
import os
from time import time
import pyautogui as py
from window_capture import WindowCapture

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture('RuneLite')

loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()

    cv.imshow('Computer vision', screenshot)

    print('fps {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done')