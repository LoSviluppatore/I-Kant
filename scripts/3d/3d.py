import cv2 as cv
import mediapipe as mp
import json

#richiedo i moduli mediapipe per tracciare il viso e per disegnarci sopra.
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

#il primo parametro serve per il primo rilevamento, il secondo per i successivi, il terzo serve per un renderizzare in modo migliore occhi e bocca.
face_mesh = mp_face_mesh.FaceMesh(
    min_detection_confidence = 0.6,
    min_tracking_confidence = 0.5,
    refine_landmarks = True,
)

#apro la videocamera 0
camera = cv.VideoCapture(0)
# frame_count = 0

while camera.isOpened():
    try:
        ret, frame = camera.read()

        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        results = face_mesh.process(rgb_frame)


# Sintesi delle Connessioni:
# FACEMESH_TESSELATION: Triangolazione completa dei punti facciali.
# FACEMESH_CONTOURS: Contorni principali del viso.
# FACEMESH_IRISES: Connessioni degli occhi (iridi).
# FACEMESH_LIPS: Connessioni intorno alla bocca.
# FACEMESH_FACE_OVAL: Contorno del viso.
# FACEMESH_LEFT_EYE: Connessioni per l'occhio sinistro.
# FACEMESH_RIGHT_EYE: Connessioni per l'occhio destro.

        if results.multi_face_landmarks:
            for landmark in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image = frame,
                    landmark_list = landmark,
                    connections = mp_face_mesh.FACEMESH_LIPS,
                    # landmark_drawing_spec = None, leva i puntini
                    landmark_drawing_spec = mp_drawing.DrawingSpec(circle_radius=1, thickness=1),
                    connection_drawing_spec = mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=1)
                )

        cv.imshow("I-kant_extract_face_mesh", frame)

        #dopo un millisecondo confronta il tasto premuto, se è e esci dal ciclo
        if cv.waitKey(1) & 0xFF == ord('e'):
            break


    except Exception as e:
        print(e)
        break

camera.release()
cv.destroyAllWindows()
