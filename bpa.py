#finding the body angles using math for each body part
#imports
import mediapipe as mp
import pandas as pd
import numpy as np
import cv2
from stuff import *


class BPA:
    #set init
    def __init__(self, landmarks):
        self.landmarks = landmarks

    def left_leg(self):
        #hip
        h = find(self.landmarks, "LEFT_HIP")
        #knee
        k = find(self.landmarks, "LEFT_KNEE")
        #ankle
        a = find(self.landmarks, "LEFT_ANKLE")
        return calc(h, k, a)

    def right_leg(self):
        h = find(self.landmarks, "RIGHT_HIP")
        k = find(self.landmarks, "RIGHT_KNEE")
        a = find(self.landmarks, "RIGHT_ANKLE")
        return calc(h, k, a)

    def abdomen(self):
        # left right shoulder
        ls = find(self.landmarks, "LEFT_SHOULDER")
        rs = find(self.landmarks, "RIGHT_SHOULDER")

        # left right hip
        lh = find(self.landmarks, "LEFT_HIP")
        rh = find(self.landmarks, "RIGHT_HIP")

        # left right knee
        lk = find(self.landmarks, "LEFT_KNEE")
        rk = find(self.landmarks, "RIGHT_KNEE")

        #averages
        sa = [(rs[0] + ls[0]) / 2,(rs[1] + ls[1]) / 2]
        ha = [(rh[0] + lh[0]) / 2, (rh[1] + lh[1]) / 2]
        ka = [(rk[0] + lk[0]) / 2, (rk[1] + lk[1]) / 2]

        return calc(sa, ha, ka)
    
    def left_arm(self):
        #shoulder
        s = find(self.landmarks, "LEFT_SHOULDER")
        #elbow
        e = find(self.landmarks, "LEFT_ELBOW")
        #wrist
        w = find(self.landmarks, "LEFT_WRIST")
        return calc(s, e, w)

    def right_arm(self):
        s = find(self.landmarks, "RIGHT_SHOULDER")
        e = find(self.landmarks, "RIGHT_ELBOW")
        w = find(self.landmarks, "RIGHT_WRIST")
        return calc(s, e, w)
