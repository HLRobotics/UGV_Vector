import cv2


    #cap = cv2.VideoCapture(0) #default camera
cap = cv2.VideoCapture(0)
    
while(True):
    retrive, frame = cap.read()
    frame=cv2.resize(frame, (960, 540)) 
    cv2.imshow('Capturing',frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'): #click q to stop capturing
        break
