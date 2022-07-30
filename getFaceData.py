import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceID = input('\n enter user id end press <return> ==>  ')
count = 0

while(True):

    ret = cam.read()
	image = cam.read()
    image = cv2.flip(image, -1) 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save face to a folder
        cv2.imwrite("FaceData/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', image)

    k = cv2.waitKey(100) & 0xff # Escape Key
    if k == 27:
        break
    elif count >= 50: # 50 images to train 
         break

cam.release()
cv2.destroyAllWindows()