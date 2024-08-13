import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
def findClickPosition(invent_img_path, fish_image_path, threshold=0.4, debug_mode=None):
    invent_img = cv.imread(invent_img_path, cv.IMREAD_UNCHANGED)
    fish_img = cv.imread(fish_image_path, cv.IMREAD_UNCHANGED)

    fish_w = fish_img.shape[1]
    fish_h = fish_img.shape[0]

    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(invent_img, fish_img, method)

    threshold = 0.8
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), fish_w, fish_h]
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
    # print(rectangles)
    points = []
    if len(rectangles):
        print('image found')

        fish_w = fish_img.shape[1]
        fish_h = fish_img.shape[0]
        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        for (x, y, w, h) in rectangles:
            # change to random location in a square
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            points.append((center_x, center_y))

            if debug_mode == 'rectangles':
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                cv.rectangle(invent_img, top_left, bottom_right, line_color, line_type)

            elif debug_mode == 'points':
                cv.drawMarker(invent_img, (center_x, center_y), marker_color)

        if debug_mode:
            cv.imshow('matches', invent_img)
            cv.waitKey()

    return points
points = findClickPosition('./images/fishing_invent.png', './images/leaping_salmon.png', debug_mode='points')
print(points)