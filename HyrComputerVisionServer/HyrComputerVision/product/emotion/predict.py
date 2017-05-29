#coding:utf8
'''
Created on 2017年5月22日

@author: Administrator
'''
import numpy as np
import urllib
import cv2
from sklearn.externals import joblib
import gabor_nn_clf
import dlib
import os
#clf = gabor_nn_clf.gabor_nn_clf()

detector = dlib.get_frontal_face_detector()
def init_data(gray, (x, y, w, h)):
    gray = gray[y:y+h, x:x+w]
    gray = cv2.resize(gray, (48, 48))
    gray = cv2.equalizeHist(gray)
    X = gray.reshape((1, 48*48))

    return X

def predict_one_face(img, face):
    clf = joblib.load(os.getcwd() + "/HyrComputerVisionServer/HyrComputerVisionServer/HyrComputerVision/product/model_for_detect/pipe_nn.pkl")
    X = init_data(img, face)
    #3=Happy, 4=Sad, 5=Surprise, 6=Neutral
    arr = clf.predict_proba(X)[0]
    return {'happiness':arr[0], 'neutral':arr[3], 
             'sadness':arr[1], 'surprise':arr[2]}
    
def detect_face(gray):

    cascPath = os.getcwd() + "/HyrComputerVisionServer/HyrComputerVisionServer/HyrComputerVision/product/model_for_detect/haarcascade_frontalface_alt.xml"
    faceCascade = cv2.CascadeClassifier(cascPath) 
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize=(64, 64)
    )
   
    return faces

def read_image(url):
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def get_result(url):
    image = read_image(url)
    res = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    max = gray.shape[0] if gray.shape[0] > gray.shape[1] else gray.shape[1]
    if max > 500:
        if max == gray.shape[0]:
            gray = cv2.resize(gray, (gray.shape[1]*500/max, 500))
        if max == gray.shape[1]:
            gray = cv2.resize(gray, (500, gray.shape[0]*500/max))
    faces = detect_face(gray)
    
    for (x, y, w, h) in faces:
        res.append({'face_rectangle':{'top':y, 'left':x, 'width':w,'height':h},
                    'scores':predict_one_face(gray, (x, y, w, h))})
    return res

def get_file_result(file_path):
    image = cv2.imread(file_path)
    res = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    max = gray.shape[0] if gray.shape[0] > gray.shape[1] else gray.shape[1]
    if max > 500:
        if max == gray.shape[0]:
            gray = cv2.resize(gray, (gray.shape[1]*500/max, 500))
        if max == gray.shape[1]:
            gray = cv2.resize(gray, (500, gray.shape[0]*500/max))
    
    faces = detect_face(gray)
   
    for (x, y, w, h) in faces:
        res.append({'face_rectangle':{'top':y, 'left':x, 'width':w,'height':h},
                    'scores':predict_one_face(gray, (x, y, w, h))})
    return res