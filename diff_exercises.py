#classifying the different exercises
#imports
import numpy as np
from bpa import BPA
from stuff import *

#get the exercise type
class EXTYPE(BPA):
    #set init
    def __init__(self, lm):
        super().__init__(lm)

    #situps check abdomen angle
    def sit_up(self, cnt, flag):
        angle = self.abdomen()
        if flag and angle < 55:
            cnt += 1
            flag = False
        elif flag == False and angle > 105:
            flag = True

        return [cnt, flag]

    #for pushups check arm angle
    def push_up(self, cnt, flag):
        avg = (self.left_arm() + self.right_arm()) / 2
        if flag and avg < 70:
            cnt += 1
            flag = False
        elif flag == False and avg > 160:
            flag = True

        return [cnt, flag]

    #for pull ups check elbow and face angle
    def pull_up(self, cnt, flag):
        nose = find(self.landmarks, "NOSE")
        le = find(self.landmarks, "LEFT_ELBOW")
        re = find(self.landmarks, "RIGHT_ELBOW")
        avg = (le[1] + re[1]) / 2

        if flag and nose[1] > avg:
            cnt += 1
            flag = False

        elif flag == False and nose[1] < avg:
            flag = True

        return [cnt, flag]

    #squat check leg angle
    def squat(self, cnt, flag):
        avg = (self.right_leg()+ self.left_leg()) / 2

        if flag and avg < 70:
            cnt += 1
            flag = False
        elif flag == False and avg>160:
            flag = True

        return [cnt, flag]

    #find the exercise
    def excalc(self, extype, cnt, flag):
        if extype == "sit-up":
            cnt, flag = EXTYPE(self.landmarks).sit_up(cnt, flag)
        elif extype == "push-up":
            cnt, flag = EXTYPE(self.landmarks).push_up(cnt, flag)
        elif extype == "squat":
            cnt, flag = EXTYPE(self.landmarks).squat(cnt, flag)
        elif extype == "pull-up":
            cnt, flag = EXTYPE(self.landmarks).pull_up(cnt, flag)

        return [cnt, flag]
