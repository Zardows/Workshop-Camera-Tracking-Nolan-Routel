#!/usr/bin/env python3
import cv2
import mediapipe as mp


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

def detect_hand():
    cam = cv2.VideoCapture(0)
    mpHand = mp.solutions.hands
    hands = mpHand.Hands()
    while True:
        ret, frame = cam.read()
        if not ret:
            print("unable to open camera")
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        print(results.multi_hand_landmarks)
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def draw_plan():
    cam = cv2.VideoCapture(0)
    mpHand = mp.solutions.hands
    hands = mpHand.Hands()
    mpDraw = mp.solutions.drawing_utils
    while True:
        ret, frame = cam.read()
        if not ret:
            print("unable to open camera")
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        if results.multi_hand_landmarks:
            for handlms in results.multi_hand_landmarks:
                for id, lm in enumerate(handlms.landmark):
                    h, w, c = frame.shape
                    x, y = int(lm.x * w), int(lm.y * h)
                results.draw_landmarks(frame, handlms)
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

open_video()