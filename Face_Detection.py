import cv2
from random import randrange

# haar cascade algorithm used to detect objects in images
# Can be faces,bodies and coca colas!
# Link to github file:
# https://github.com/opencv/opencv
# This project aims to make a face detection using Python


# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.txt')

# Chose an image to detect faces in
# img = cv2.imread('IMG_57654846153F-1.jpeg')
# To Capture video from webcam ((0 is the default cam))
webcam = cv2.VideoCapture(0)


# Iterate forever over frames
while True: 

    ### Read the current frame (bool,image)
    successful_frame_read ,frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # DetectMutliScale --> Detects objects of different sizes in the input image. The detected objects returned as list of rectangles. 
    # Top left point, to get bottom right x,y,w,h --> x+w , y+h
    face_coordiantes = trained_face_data.detectMultiScale(grayscaled_img)

    #Looping over it, purpose if there is more than one face 
    for(x,y,w,h) in face_coordiantes:
        ### Four paramater; the image, upper left coordinates, bottom right coordinates, color and thikness
         cv2.rectangle(frame , (x,y),(x+w,y+h), (0,0,255),3)

    cv2.imshow('Facer Detector',frame)
    key = cv2.waitKey(1)
    
    #Q or q
    if key == 81 or key == 113: 
        break

### Realse the VideoCaputre 
webcam.release()


print("Code Completed!") 

