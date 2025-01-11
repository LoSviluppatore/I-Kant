import cv2 as cv
import json
import numpy as np
import pickle


with open('landmarks.pkl', 'rb') as landmark_file:
    face_landmarks_data = pickle.load(landmark_file)


frame_width, frame_height = 640, 480

# image_frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

# for landmark in face_landmarks_data:
#     if landmark['frame'] == 1:
#         cv.circle(image_frame, (int(landmark['x'] * frame_width), int(landmark['y'] * frame_height)), 2, (255, 0, 0), -1)

# cv.imshow("frame", image_frame)

# cv.waitKey(0)
# cv.destroyAllWindows()


frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)  # Crea un frame nero
last_frame = None
points_by_frame = {}

def getPoint(landmark):
    return (int(landmark['x'] * frame_width), int(landmark['y'] * frame_height))

def drawLandmarks():
    #prendi il numero dei frame e se per ogni landmark il numero non è nel dizionario crei la key vuota con il frame_num, pou metti nel dizionario a indice frame_num il punto del landmark<
    for landmark in face_landmarks_data:
        frame_num = landmark['frame']
        if frame_num not in points_by_frame:
            points_by_frame[frame_num] = []
        points_by_frame[frame_num].append(getPoint(landmark))

    #per ogni frame_num nel dizionario ricrei il frame e inizializzi i punti nuovi per poi disegnarli per ogni punto
    for frame_num in points_by_frame:
        frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
        points = points_by_frame[frame_num]

        for point in points:
            cv.circle(frame, point, 2, (255, 255, 255), -1)
        
        cv.imshow("face landmarks", frame)

        #30 sarebbe tipo il frame_rate
        if cv.waitKey(30) & 0xFF == ord('e'):
            break

    cv.destroyAllWindows()


drawLandmarks()