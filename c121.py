import cv2
import time
import numpy as np

#To save the output in a file output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

#Starting the webcam
cap = cv2.VideoCapture(0)

#Allowing the webcam to start by making the code sleep for 2 seconds
time.sleep(2)
bg = 0

#Capturing background for 60 frames
for i in range(60):
    ret, bg = cap.read()
#Flipping the backgroundpi
bg = np.flip(bg, axis=1)

#Reading the captured frame until the camera is open
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
   

    frame=cv2.resize(frame,(640,480))
    image=cv2.resize(image,(640,480))

    #Generating mask to detect black colour
    #These values can also be changed as per the color

    lower_black = np.array([30, 30, 0])
    upper_black = np.array([104,153,70])

    mask = cv2.inRange(frame, lower_black, upper_black)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    f = frame - res
    f = np.where(f == 0, image, f)


cap.release()
out.release()
cv2.destroyAllWindows()
