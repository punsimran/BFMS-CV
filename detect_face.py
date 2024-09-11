import cv2
import face_recognition
import pickle
import numpy as np


# --- Load Trained Model ---
encodings_file = "trained_encodings2.pkl" 
try:
    with open(encodings_file, "rb") as f:
        loaded_data = pickle.load(f)
    known_face_encodings = loaded_data["encodings"]
    known_face_names = loaded_data["names"]
except FileNotFoundError:
    print("Error: Trained encodings file not found. Run train_model.py first.")
    exit()

# --- Face Detection ---
face_locations = []
face_encodings = []
process_this_frame = True
similarity_threshold = 0.8

video_capture = cv2.VideoCapture(0)  


while True:
    ret, frame = video_capture.read()
    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []

        for face_encoding in face_encodings:
            distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(distances)
            
            if distances[best_match_index] <= similarity_threshold:
                name = known_face_names[best_match_index]
            else:
                name = "Unknown"
                
            face_names.append(name)
            print(name)
    process_this_frame = not process_this_frame

    # Display results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

# import cv2
# import face_recognition
# import pickle

# # --- Load Trained Model ---
# encodings_file = "trained_encodings2.pkl"
# try:
#     with open(encodings_file, "rb") as f:
#         loaded_data = pickle.load(f)
#     known_face_encodings = loaded_data["encodings"]
#     known_face_names = loaded_data["names"]
# except FileNotFoundError:
#     print("Error: Trained encodings file not found. Run train_model.py first.")
#     exit()

# # --- Face Detection ---
# video_capture = cv2.VideoCapture(0)
# face_locations = []
# face_encodings = []
# face_names = []
# process_this_frame = True

# while True:
#     ret, frame = video_capture.read()
#     if process_this_frame:
#         # Resize frame to 1/4 size for faster face recognition processing
#         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#         rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#         # Find all face locations and face encodings in the current frame
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#         face_names = []
#         for face_encoding in face_encodings:
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.4)
#             face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#             best_match_index = face_distances.argmin() if len(face_distances) > 0 else None
#             name = "Unknown"

#             # Check if a match was found in known_face_encodings
#             if best_match_index is not None and matches[best_match_index]:
#                 similarity = (1 - face_distances[best_match_index]) * 100  # Calculate similarity percentage
#                 if similarity >= 80:  # Apply the threshold for 80% similarity
#                     name = known_face_names[best_match_index]
#                     print(f"Match found: {name} with {similarity:.2f}% similarity")
#                 else:
#                     print(f"Similarity {similarity:.2f}% is below threshold for {known_face_names[best_match_index]}")

#             face_names.append(name)

#     process_this_frame = not process_this_frame

#     # Display the results
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         top *= 4
#         right *= 4
#         bottom *= 4
#         left *= 4

#         # Draw a rectangle around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
#         cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

#     # Display the resulting image
#     cv2.imshow('Video', frame)

#     # Hit 'q' on the keyboard to quit the video capture
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release handle to the webcam
# video_capture.release()
# cv2.destroyAllWindows()




