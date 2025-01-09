import mediapipe as mp
from utils import serializeObj

#richiedo i moduli mediapipe per tracciare il viso e per disegnarci sopra.
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

#il primo parametro serve per il primo rilevamento, il secondo per i successivi, il terzo serve per un renderizzare in modo migliore occhi e bocca.
face_mesh = mp_face_mesh.FaceMesh(
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5,
    refine_landmarks = True,
)

landmark_points = []

class Landmarking:
    # def __init__(self, results):
    #     self.results = results

    @staticmethod
    def drawLandmarks(results, frame):
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
                    connections = mp_face_mesh.FACEMESH_TESSELATION,
                    # landmark_drawing_spec = None, #leva i puntini
                    landmark_drawing_spec = mp_drawing.DrawingSpec(circle_radius=1, thickness=1),
                    # connection_drawing_spec = mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
                )

    @staticmethod
    def extract_landmarks(results, frame_count):
        if results.multi_face_landmarks:
        #     try:
            for face_landmarks in results.multi_face_landmarks:
                # landmark_points = []
                for landmark in face_landmarks.landmark:
                    landmark_points.append({
                        'frame': frame_count,
                        'x': landmark.x,
                        'y': landmark.y
                    })
                    # print(landmark_points)
                # for connection in mp_face_mesh.FACEMESH_TESSELATION:

                #     # print(connection)
                #     start_index, end_index = connection
                #     start_point = landmark.landmark[start_index]
                #     end_point = landmark.landmark[end_index]

                #     landmark_points.append({
                #         'start': {'x': start_point.x, 'y': start_point.y, 'z': start_point.z},
                #         'end': {'x': end_point.x, 'y': end_point.y, 'z': end_point.z}
                #     })
        return landmark_points

            # except Exception as error:
            #     return error
