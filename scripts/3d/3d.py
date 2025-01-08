import cv2 as cv
import json
from landmarking import *
from utils import serializeObj, deserializeObj

#apro la videocamera 0
camera = cv.VideoCapture(0)

#var frame_count per rallentare il processo
frame_count = 0

while camera.isOpened():
    frame_count += 1
    if len(landmark_points) >= 10:
        serializeObj(landmark_points)
        for el in deserializeObj():
            print (el)
        break
    
    try:
        ret, frame = camera.read()

        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        results = face_mesh.process(rgb_frame)


        Landmarking.drawLandmarks(results, frame)


        if frame_count % 8 == 0: #molto lento, ma è una prova
            Landmarking.extract_landmarks(results)

            frame_count = 0


        cv.imshow("I-kant_extract_face_mesh", frame)

        #dopo un millisecondo confronta il tasto premuto, se è e esci dal ciclo
        if cv.waitKey(1) & 0xFF == ord('e'):
            break


    except Exception as e:
        print(e)
        break

camera.release()
cv.destroyAllWindows()