import cv2
import os
import time

#####################################
from cv2 import FONT_HERSHEY_SIMPLEX

cameraNo = 1
cameraBrightness = 190
moduleValue = 10
minBlur = 500
grayImage = False
saveData = True
ShowImage = True
imgWidth = 400
imgWeight = 400

#######################################

ResistorCascade = cv2.CascadeClassifier("Resources/resistorCascade.xml")
img = cv2.imread('Resources/002.jpg')
img = cv2.resize(img, (imgWidth, imgWeight))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("not Result", img)

Resistor = ResistorCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in Resistor:
    if w > 134:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "Resistor", (x, y), FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
# 008
# 012