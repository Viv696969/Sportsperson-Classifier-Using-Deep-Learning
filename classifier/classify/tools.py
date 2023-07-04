import pickle
from tensorflow import keras
import numpy as np
import cv2 as cv


face_cascade = None
eye_cascade = None
model=None
classes=None

def get_predictions(y):
    l=[]
    for i in y:
        val=np.argmax(i)
        l.append(classes[val])
    return l


def get_cropped_image(image):
    img=cv.imread(image)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     now read the face
    face=face_cascade.detectMultiScale(gray)
    for x,y,w,h in face:
        roi_img=img[y:y+h,x:x+h]
        roi_gray=gray[y:y+h,x:x+h]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        if len(eyes)>=2:
            return roi_img
        else:
            return None

def classify_image(image=None,path=None):
    if image==None:
        return False,False
    img=get_cropped_image(image)
    try:
        if img.any():
            
        
            # resize the image
            img=cv.resize(img,(128,128))  
            # scaling the image
            img=img/255

            probablities=model.predict(np.expand_dims(img,0))
            class_name=get_predictions(probablities)
            
            return np.round(probablities*100,2),class_name
            
        else:
            return False,False
    except:
        return False,False
    
 


def load_objects():
    print("load objects")
    global model,classes,face_cascade,eye_cascade

    model=keras.models.load_model('./models/sportspersonmodel.h5')
    
    f=open('./models/class_array.pickle','rb')
    classes=pickle.load(f)
    
    f.close() 
    face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
    print("objects loaded")

if __name__=='__main__':
    load_objects()
    classify_image(path='images.jpg')