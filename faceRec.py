import cv2 as cv

cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
facePic = cv.imread('facePic.jpg')
grayScale = cv.cvtColor(facePic, cv.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(grayScale, 1.1, 4)
for (x, y, w, h) in faces:
    cv.rectangle(facePic, (x, y), (x+w, y+h), (0, 0, 255), 2)
cv.imshow('facePic', facePic)
cv.waitKey()


a data block can be 64 bits large, 16 bits for each register and 16 for an instruction. 



a. 36,000 times

b. .10 * 60 minutes = 6 minutes of typing. 

    30 words a minute for 6 minutes = 180

    180 words at 5 letters a word = 900 keys

    179 spaces between each word = 1079 keystrokes for one hour

c.  1079 / 36000 = about 3/100