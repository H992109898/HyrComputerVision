#coding:utf8
'''
Created on 2017年5月28日

@author: Administrator
'''
import dlib
import os
import numpy as np
PREDICTOR_PATH = os.getcwd() +"/HyrComputerVisionServer/HyrComputerVisionServer/HyrComputerVision/product/model_for_detect/shape_predictor_68_face_landmarks.dat"    
predictor = dlib.shape_predictor(PREDICTOR_PATH)  

def predict(image, rect):
    return [[p.x,p.y] for p in predictor(image,rect).parts()]
    
        