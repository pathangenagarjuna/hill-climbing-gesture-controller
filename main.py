import mediapipe as mp
import cv2
import pydirectinput

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as holistic:
    while cap.isOpened():
        success, img = cap.read()
        img = cv2.flip(img,1)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = holistic.process(img)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        height, width, _ = img.shape

        try:
            right_hand = (results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * width,
                          results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * height)
            y_mid = height // 2

            pose = "move"
            if (right_hand[1] < y_mid):
                pose = "acc"
                pydirectinput.keyDown('right')
                pydirectinput.keyUp('left')
            elif (right_hand[1] > y_mid):
                pose = "brake"
                pydirectinput.keyDown('left')
                pydirectinput.keyUp('right')
        except:
            pass
        cv2.putText(img, pose, (20, 8), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)
        cv2.line(img, (0,y_mid),(width,y_mid),(255,0,255),2)
        cv2.imshow("Hand Controller", img)
        if cv2.waitKey(1) == ord('q'):
            break;
cap.release()
cv2.destroyAllWindows()