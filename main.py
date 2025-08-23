import cv2
from simple_facerec import SimpleFacerec

#Encode faces from a folder
sfr=SimpleFacerec()
sfr.load_encoding_images("C:/project/images")

#Load Camera


# Start video capture from the default camera
cap = cv2.VideoCapture(0)

# Loop to continuously capture frames from the camera
while True:
    ret, frame = cap.read()  # Read a frame from the camera
    if not ret:
        break  # Break the loop if there is an issue with the camera   

    #Detect Faces
    face_locations, face_names=sfr.detect_known_faces(frame)
    for face_loc ,name in zip(face_locations,face_names):
        y1,x2,y2,x1=face_loc[0],face_loc[1],face_loc[2],face_loc[3]

        cv2.putText(frame, name , (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1,(0,0,200), 2)
        cv2.rectangle(frame, (x1,y1) , (x2,y2) , (0,0,200) , 2)

    cv2.imshow("Frame", frame)
     # Check if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Camera turned off. 'q' key pressed.")
        break  # Exit the loop when 'q' is pressed

# Release the video capture object and close any open windows

    
cap.release()
cv2.destroyAllWindows()