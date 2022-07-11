import cv2
import numpy as np 

fourcc = cv2.VideoWriter_fourcc(*'XVID')
frame_1 = cv2.VideoWriter('final.avi', fourcc, 20.0, (640, 480))

image = cv2.imread("bg.jpg")
bg = 0
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0]) 

    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    f = frame - res
    f = np.where(f == 0, image, f)

    final_output = cv2.addWeighted(f, 1, f, 1, 0)
    frame_1.write(final_output)

    cv2.imshow('blackscreen', frame)
    cv2.imshow('mask', f)

    k = cv2.waitKey(5) 
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()