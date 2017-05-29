#coding:utf8
'''
Created on 2017年5月28日

@author: Administrator
'''
import urllib
import numpy as np
import cv2
import dlib
import landmark


detector = dlib.get_frontal_face_detector()  

def detect_face(gray):
    return detector(gray,1)

def read_image(url):
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def get_result(url):
    image = read_image(url)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    max = gray.shape[0] if gray.shape[0] > gray.shape[1] else gray.shape[1]
    if max > 500:
        if max == gray.shape[0]:
            gray = cv2.resize(gray, (gray.shape[1]*500/max, 500))
        if max == gray.shape[1]:
            gray = cv2.resize(gray, (500, gray.shape[0]*500/max))
    faces = detect_face(gray)
    res = []
    for rect in faces:
        res.append({'face_rectangle':{'top':rect.top(), 'left':rect.left(), 'width':rect.width(),'height':rect.height()},
                    'landmarks':landmark.predict(gray, rect)})
        #landmark.predict(gray, rect)
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
   
    for rect in faces:
        res.append({'face_rectangle':{'top':rect.top(), 'left':rect.left(), 'width':rect.width(),'height':rect.height()},
                    'landmarks':landmark.predict(gray, rect)})
    return res