import cv2 as cv
import json
import numpy as np
import pickle


with open('landmarks.pkl', 'rb') as f:
    face_landmarks_data = pickle.load(f)


frame_width, frame_height = 640, 480

# image_frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

# for landmark in face_landmarks_data:
#     if landmark['frame'] == 1:
#         cv.circle(image_frame, (int(landmark['x'] * frame_width), int(landmark['y'] * frame_height)), 2, (255, 0, 0), -1)

# cv.imshow("frame", image_frame)

# cv.waitKey(0)
# cv.destroyAllWindows()


# out = cv.VideoWriter('face_landmarks_video.avi', cv.VideoWriter_fourcc(*'XVID'), 20, (frame_width, frame_height))

frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)  # Crea un frame nero

last_frame = None

#prova a fare per ogni frame disegna i landmark

for landmark in face_landmarks_data:

    if landmark['frame'] != last_frame:
        frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    
    point = (int(landmark['x'] * frame_width), int(landmark['y'] * frame_height))
    cv.circle(frame, point, 2, (255, 0, 0), -1)


    cv.imshow("frame_2", frame)

    last_frame = landmark['frame']

    
    if cv.waitKey(1) & 0xFF == ord('e'):
        break


cv.destroyAllWindows()
