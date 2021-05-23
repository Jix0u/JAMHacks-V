#this is the utils aka stuff
#imports
import mediapipe as mp
import pandas as pd
import numpy as np
import cv2

mpp = mp.solutions.pose

#to show the table
def tble(exercise, cnt, stat):
    tble = cv2.imread("/Users/leonachen/Desktop/ExerciseAI/images/Exercise Panel.png")
    cv2.putText(tble, "Exercise : " + exercise.replace("-", " "), (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (219, 103, 232), 2, cv2.LINE_AA)
    cv2.putText(tble, "Count : " + str(cnt), (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (219, 103, 232), 2, cv2.LINE_AA)
    cv2.putText(tble, "Stat : " + str(stat), (20, 145), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (219, 103, 232), 2, cv2.LINE_AA)
    cv2.imshow("Exercise Panel", tble)

#calculate the angle between 3 values
def calc(a, b, c):
    #get numpy array of each value aka each coordinate
    a = np.array(a)  
    b = np.array(b)  
    c = np.array(c)  
    #take y coord of c - y coord of b then divide by x coord of c - x coord of b then take arc tan of that value 
    rad = np.arctan2(c[1] - b[1], c[0] - b[0]) -\
              np.arctan2(a[1] - b[1], a[0] - b[0])
    #convert to degrees
    angle = np.abs(rad * 180.0 / np.pi)

    #if the angle is bigger than 180 take 360 - angle cuz it has to be less
    if angle > 180.0:
        return 360 - angle
    return angle

#find the angle from the landmarks given a name
def find(lm, name):
    return [
        lm[mpp.PoseLandmark[name].value].x,
        lm[mpp.PoseLandmark[name].value].y,
        lm[mpp.PoseLandmark[name].value].visibility
    ]


