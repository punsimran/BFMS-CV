# import cv2
# import face_recognition
# import os
# import pickle

# # --- Training Configuration ---
# trained_dataset_dir = "cropped_data"  
# encodings_file = "trained_encodings2.pkl"

# # --- Training Phase ---
# known_face_encodings = []
# known_face_names = []

# print("Starting training...")
# for foldername in os.listdir(trained_dataset_dir):
#     folder_path = os.path.join(trained_dataset_dir, foldername)
#     if os.path.isdir(folder_path):  # Ensure it's a directory
#         print(f"Processing folder: {foldername}")
#         for filename in os.listdir(folder_path):
#             if filename.endswith((".jpg", ".jpeg", ".png")):
#                 image_path = os.path.join(folder_path, filename)
#                 print(f"Processing image: {image_path}")
                
#                 # Load the image
#                 image = face_recognition.load_image_file(image_path)
                
#                 # Find face locations and encodings
#                 face_locations = face_recognition.face_locations(image)
#                 print(f"Found {len(face_locations)} face(s) in {filename}")
                
#                 face_encodings = face_recognition.face_encodings(image, face_locations)[0] if face_recognition.face_encodings(image,face_locations) else None
#                 if face_encodings is not None:
#                     # for face_encoding in face_encodings:
#                     known_face_encodings.append(face_encodings[0])
#                     known_face_names.append(foldername)  # Use folder name as the face name
#                     print(f"Added {len(face_encodings)} encoding(s) for {filename}")
#                 else:
#                     print(f"Warning: No face detected in {filename}. Skipping...")

# # Save the encodings
# print("Saving encodings to", encodings_file)
# with open(encodings_file, "wb") as f:
#     pickle.dump({"encodings": known_face_encodings, "names": known_face_names}, f)

# print("Training complete!")

import os
import face_recognition
import pickle

# --- Training Configuration ---
trained_dataset_dir = "cropped_data"  
encodings_file = "trained_encodings2.pkl"

# --- Training Phase ---
known_face_encodings = []
known_face_names = []

print("Starting training...")
for foldername in os.listdir(trained_dataset_dir):
    folder_path = os.path.join(trained_dataset_dir, foldername)
    if os.path.isdir(folder_path):  # Ensure it's a directory
        print(f"Processing folder: {foldername}")
        for filename in os.listdir(folder_path):
            if filename.endswith((".jpg", ".jpeg", ".png",".JPG")):
                image_path = os.path.join(folder_path, filename)
                print(f"Processing image: {image_path}")
                
                # Load the image
                image = face_recognition.load_image_file(image_path)
                
                # Find face locations and encodings
                face_locations = face_recognition.face_locations(image)
                print(f"Found {len(face_locations)} face(s) in {filename}")
                
                face_encodings = face_recognition.face_encodings(image, face_locations)
                if face_encodings:
                    # Corrected: add each encoding individually to the list
                    for face_encoding in face_encodings:
                        known_face_encodings.append(face_encoding)
                        known_face_names.append(foldername)  # Use folder name as the face name
                    print(f"Added {len(face_encodings)} encoding(s) for {filename}")
                else:
                    print(f"Warning: No face detected in {filename}. Skipping...")

# Save the encodings
print("Saving encodings to", encodings_file)
with open(encodings_file, "wb") as f:
    pickle.dump({"encodings": known_face_encodings, "names": known_face_names}, f)

print("Training complete!")
