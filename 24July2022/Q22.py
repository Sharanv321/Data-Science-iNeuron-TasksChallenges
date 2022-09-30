# Q22) write a function which can read video file and play for you .

import cv2
# Creating a function to play the video

def playvideo(path):

    cap = cv2.VideoCapture(path)

    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)
        cv2.waitKey(10)

    cap.release()
    cv2.destroyAllWindows()