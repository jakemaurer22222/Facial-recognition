import cv2
import numpy as np
from PIL import Image
import os

path = 'FaceData'

recognizeComponent = cv2.face.LBPHFaceRecognizer_create()
detectorComponent = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# function to get the images and label data
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detectorComponent.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

faces = getImagesAndLabels(path)
ids = getImagesAndLabels(path)
recognizeComponent.train(faces, np.array(ids))

# Save
recognizeComponent.write('trainer/trainer.yml')
