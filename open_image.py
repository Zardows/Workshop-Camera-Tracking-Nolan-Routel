#!/usr/bin/env python3
import cv2


def open_image():
    img = cv2.imread('bbb.jpg')

    while True:
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def open_video():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        cv2.imshow("Image", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

open_video()