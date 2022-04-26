from re import template
import pyautogui as pg
import cv2
import time
import os
from matplotlib import pyplot as plt
import keyboard

# must be run in terminal


rocks = os.listdir("Rocks")

while True:
    movex, movey, movew, moveh = 670, 390, 270, 270
    screenshot = pg.screenshot("screenshot.png", (movex, movey, movew, moveh))

    img_rgb = cv2.imread("screenshot.png", 0)
    img = img_rgb.copy()
    template = cv2.imread("COMBO3.PNG", 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    #top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    print(top_left, bottom_right)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    x = (bottom_right[0] + top_left[0])/2 + movex
    y = (bottom_right[1] + top_left[1])/2 + movey
    comboPos = x, y
    pg.click(comboPos)
    if keyboard.is_pressed("b"):
        break

"""
plt.subplot(121),plt.imshow(res, cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img, cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle("meth")
plt.show()
"""