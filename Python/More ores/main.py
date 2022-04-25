import pyautogui as pg
import cv2
import numpy as np
import time

time.sleep(2)
# must be run in terminal
screenshot = pg.screenshot("screenshot.png")

screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

stone = pg.locateOnScreen("cobelstone.png")
print(pg.size())
cv2.rectangle(screenshot, (stone.left, stone.top), (stone.left + stone.width, stone.top + stone.height), (0, 255, 255), 2)

x, y = pg.locateCenterOnScreen("cobelstone.png")
rockPos = x/2, y/2
pg.moveTo(rockPos)
for x in range(3):
    pg.drag(0, 1, 5, button='left') 

cv2.imshow("Screenshot", screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()