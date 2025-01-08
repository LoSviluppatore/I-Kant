import pickle


def deserializeObj():
    try:
        with open("landmarks.pkl", "rb") as landmark_file:
            landmarks = pickle.load(landmark_file)
            print("landmarks deserialized correctly")
            return landmarks
    except Exception as e:
        print(e)
        return []

    
def serializeObj(landmarks):
    landmarks_list = deserializeObj()
    with open('landmarks.pkl', 'wb') as landmark_file:
        for landmark in landmarks:
            landmarks_list.append(landmark)
        pickle.dump(landmarks_list, landmark_file)
        print("landmark serialized correctly")

