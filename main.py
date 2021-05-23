#REFERENCED MEDIAPIPE https://google.github.io/mediapipe/solutions/pose.html pose solutions
import cv2
import argparse
from stuff import *
import mediapipe as mp
from bpa import BPA
from diff_exercises import EXTYPE

#add arguements for cam or from another vd
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--extype", type=str, required=True)
ap.add_argument("-v","--video", type=str, required=False)
args = vars(ap.parse_args())

#if there is no other vid source do cam
if args["video"] is not None:
    cp = cv2.VideoCapture(args["video"])
else:
    cp = cv2.VideoCapture(0) 

cp.set(3, 800) 
cp.set(4, 480) 

#get pose solutions from mediapipe api
mpp = mp.solutions.pose

with mpp.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    #add a counter for the number of squats/push-ups etc.
    mpd = mp.solutions.drawing_utils
    cnt = 0 
    stat= True 
    #when cam is opened 
    while cp.isOpened():
        ret, img = cp.read()
        #resize it
        img = cv2.resize(img, (800, 480), interpolation=cv2.INTER_AREA)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img.flags.writeable = False

        res = pose.process(img)
        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        #try getting an exercise position otherwise pass
        try:
            lm = res.pose_landmarks.landmark
            cnt, stat = EXTYPE(lm).excalc(
                args["extype"], cnt, stat)
        except:
            pass

        tble(args["extype"], cnt, stat)
        #draw the landmarks
        mpd.draw_landmarks(
            img,
            res.pose_landmarks,
            mpp.POSE_CONNECTIONS,
            mpd.DrawingSpec(color=(255, 255, 255),
                                   thickness=4,
                                   circle_radius=3),
            mpd.DrawingSpec(color=(174, 180, 45),
                                   thickness=4,
                                   circle_radius=2),
        )
        #show the vid and lines
        cv2.imshow('Video', img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    #quit release
    cp.release()
    cv2.destroyAllWindows()
