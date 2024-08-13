import cv2 as cv
import numpy as np
import os
from time import time
import win32gui, win32ui, win32con

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(winEnumHandler, None)
list_window_names()

# def window_capture():
#     w = 1920
#     h = 1080
#     hwnd = win32gui.FindWindow(None, 'RuneLite')

#     wDC = win32gui.GetWindowDC(hwnd)
#     dcObj = win32ui.CreateDCFromHandle(wDC)
#     cDC = dcObj.CreateCompatibleDC()
#     dataBitMap = win32ui.CreateBitmap()
#     dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
#     cDC.SelectObject(dataBitMap)
#     cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)
    
#     #save screenshot
#     # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
#     signedIntsArray = dataBitMap.GetBitmapBits(True)
#     img = np.fromstring(signedIntsArray, dtype='uint8')
#     img.shape = (h, w, 4)
    
#     dcObj.DeleteDC()
#     cDC.DeleteDC()
#     win32gui.ReleaseDC(hwnd, wDC)
#     win32gui.DeleteObject(dataBitMap.GetHandle())

#     img = img[...,:3]

#     img = np.ascontiguousarray(img)
#     return img

# loop_time = time()
# while(True):
#     screenshot = window_capture()

#     cv.imshow('Computer vision', screenshot)

#     print('fps {}'.format(1 / (time() - loop_time)))
#     loop_time = time()

#     if cv.waitKey(1) == ord('q'):
#         cv.destroyAllWindows()
#         break

# print('Done')
