import pyautogui as pg
import cv2
# from matplotlib import pyplot as plt
import keyboard
import time
import win32gui
import win32api
import win32con
time.sleep(1)
window = win32gui.GetForegroundWindow()
print(win32gui.GetWindowText(window))
movex, movey, movew, moveh = 670, 390, 270, 270
swordx, swordy, swordw, swordh = 20, 865, 1570, 145

def ComboAutoClick():
    pg.screenshot("combo_space.png", (movex, movey, movew, moveh))
        
    top_left, bottom_right = findObject("combo_space.png", "COMBO.PNG")
    x = (bottom_right[0] + top_left[0])/2 + movex
    y = (bottom_right[1] + top_left[1])/2 + movey
        
    comboPos = x, y
    leftClick(window, comboPos)

    if not keyboard.is_pressed("b"):
        ComboAutoClick()

def AdventureAutoClick():
    pg.screenshot("sword_space.png", (swordx, swordy, swordw, swordh))

    top_left, bottom_right = findObject("sword_space.png", "SWORD.PNG")
    x = (bottom_right[0] + top_left[0])/2 + swordx
    y = (bottom_right[1] + top_left[1])/2 + swordy

    comboPos = x, y
    leftClick(window, comboPos)
    if not keyboard.is_pressed("b"):
        AdventureAutoClick()


def leftClick(window, pos):
    lParam = win32api.MAKELONG(int(pos[0]), int(pos[1]))

    win32gui.SendMessage(window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam) 
    win32gui.SendMessage(window, win32con.WM_LBUTTONUP, 0, lParam)

def findObject(img_path, template_path):
    img_rgb = cv2.imread(img_path, 0)
    img = img_rgb.copy()
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    #top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    # print(top_left, bottom_right)
    # cv2.rectangle(img, top_left, bottom_right, 255, 2)

    return (top_left, bottom_right)

"""
plt.subplot(121),plt.imshow(res, cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img, cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle("meth")
plt.show()
"""