import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

while(True):
    screenshot = None

    cv.imshow('Computer vision', screenshot)

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
print('Done')
