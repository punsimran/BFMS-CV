import cv2
import os
import face_recognition
import random
import numpy as np
import albumentations as A  # Import Albumentations for more advanced augmentations

def augment_and_save_faces(input_dir, output_dir, flip_probability=0.5, brightness_range=(0.9, 1.1), scale_range=(0.5, 1.5), num_augmentations=7):
    """
    Detects faces, applies specific augmentations including enhanced zoom in and out, and saves results.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over each person’s folder in the input directory
    for person_name in os.listdir(input_dir):
        person_folder = os.path.join(input_dir, person_name)
        if os.path.isdir(person_folder):
            # Create a corresponding output folder for the person
            person_output_folder = os.path.join(output_dir, person_name)
            if not os.path.exists(person_output_folder):
                os.makedirs(person_output_folder)

            for filename in os.listdir(person_folder):
                if filename.endswith((".jpg", ".jpeg", ".png", ".JPG")):
                    image_path = os.path.join(person_folder, filename)
                    original_image = cv2.imread(image_path)
                    rgb_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

                    face_locations = face_recognition.face_locations(rgb_image)

                    if len(face_locations) > 0:
                        for i in range(num_augmentations):
                            augmented_image = augment_image(
                                original_image.copy(),
                                flip=random.random() < flip_probability,
                                brightness_factor=random.uniform(*brightness_range),
                                scale_factor=random.uniform(*scale_range)
                            )
                            augmented_filename = f"{os.path.splitext(filename)[0]}_aug_{i}.jpg"
                            augmented_path = os.path.join(person_output_folder, augmented_filename)
                            cv2.imwrite(augmented_path, augmented_image)

def augment_image(image, flip, brightness_factor, scale_factor):
    # Flip horizontally
    if flip:
        image = cv2.flip(image, 1)

    # Adjust brightness
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype=np.float64)
    hsv[:, :, 2] = hsv[:, :, 2] * brightness_factor
    hsv[:, :, 2][hsv[:, :, 2] > 255] = 255  # Cap brightness values at 255
    image = cv2.cvtColor(np.array(hsv, dtype=np.uint8), cv2.COLOR_HSV2BGR)

    # Scaling (Zoom In/Out)
    if scale_factor != 1.0:
        width = int(image.shape[1] * scale_factor)
        height = int(image.shape[0] * scale_factor)
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

        # Center cropping to original size
        start_x = max((image.shape[1] - width) // 2, 0)
        start_y = max((image.shape[0] - height) // 2, 0)
        end_x = start_x + width
        end_y = start_y + height
        image = image[start_y:end_y, start_x:end_x]

        # Resize back to original dimensions to maintain consistency
        original_height, original_width = image.shape[:2]
        image = cv2.resize(image, (original_width, original_height), interpolation=cv2.INTER_AREA)

    return image

# --- Configuration ---
input_image_dir = "dataset"  # Adjust with your input directory containing subfolders for each person 
output_image_dir = "cropped_data"  # Adjust with your output directory 

# --- Augmentation Settings ---
flip_probability = 0.5
brightness_range = (0.9, 1.1)  # Slightly darker and brighter
scale_range = (0.5, 1.5)  # More noticeable zoom in and out
num_augmentations = 25  # Number of augmented images per original image

# --- Run Augmentation ---
augment_and_save_faces(input_image_dir, output_image_dir,
                      flip_probability=flip_probability,
                      brightness_range=brightness_range,
                      scale_range=scale_range,
                      num_augmentations=num_augmentations)

# import cv2
# import os
# import face_recognition
# import random
# import numpy as np



# def augment_and_save_faces(input_dir, output_dir, flip_probability=0.5, brightness_range=(0.9, 1.1), scale_range=(0.5, 1.5), num_augmentations=7):
#     """
#     Detects faces, applies specific augmentations including enhanced zoom in and out, and saves results.
#     """

#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     # Iterate over each person’s folder in the input directory
#     for person_name in os.listdir(input_dir):
#         person_folder = os.path.join(input_dir, person_name)
#         if os.path.isdir(person_folder):
#             # Create a corresponding output folder for the person
#             person_output_folder = os.path.join(output_dir, person_name)
#             if not os.path.exists(person_output_folder):
#                 os.makedirs(person_output_folder)

#             for filename in os.listdir(person_folder):
#                 if filename.endswith((".jpg", ".jpeg", ".png", ".JPG")):
#                     image_path = os.path.join(person_folder, filename)
#                     original_image = cv2.imread(image_path)
#                     rgb_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

#                     face_locations = face_recognition.face_locations(rgb_image)

#                     if len(face_locations) > 0:
#                         for i in range(num_augmentations):
#                             augmented_image = augment_image(
#                                 original_image.copy(),
#                                 flip=random.random() < flip_probability,
#                                 brightness_factor=random.uniform(*brightness_range),
#                                 scale_factor=random.uniform(*scale_range)
#                             )
#                             augmented_filename = f"{os.path.splitext(filename)[0]}_aug_{i}.jpg"
#                             augmented_path = os.path.join(person_output_folder, augmented_filename)
#                             cv2.imwrite(augmented_path, augmented_image)

# def augment_image(image, flip, brightness_factor, scale_factor):
#     # Flip horizontally
#     if flip:
#         image = cv2.flip(image, 1)

#     # Adjust brightness
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     hsv = np.array(hsv, dtype=np.float64)
#     hsv[:, :, 2] = hsv[:, :, 2] * brightness_factor
#     hsv[:, :, 2][hsv[:, :, 2] > 255] = 255  # Cap brightness values at 255
#     image = cv2.cvtColor(np.array(hsv, dtype=np.uint8), cv2.COLOR_HSV2BGR)

#     # Scaling (Zoom In/Out)
#     if scale_factor != 1.0:
#         width = int(image.shape[1] * scale_factor)
#         height = int(image.shape[0] * scale_factor)
#         image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

#         # Center cropping to original size
#         start_x = max((image.shape[1] - width) // 2, 0)
#         start_y = max((image.shape[0] - height) // 2, 0)
#         end_x = start_x + width
#         end_y = start_y + height
#         image = image[start_y:end_y, start_x:end_x]

#         # Resize back to original dimensions to maintain consistency
#         original_height, original_width = image.shape[:2]
#         image = cv2.resize(image, (original_width, original_height), interpolation=cv2.INTER_AREA)

#     return image

# # --- Configuration ---
# input_image_dir = "dataset"  # Adjust with your input directory containing subfolders for each person 
# output_image_dir = "cropped_data"  # Adjust with your output directory 

# # --- Augmentation Settings ---
# flip_probability = 0.5
# brightness_range = (0.9, 1.1)  # Slightly darker and brighter
# scale_range = (0.5, 1.5)  # More noticeable zoom in and out
# num_augmentations = 25  # Number of augmented images per original image

# # --- Run Augmentation ---
# augment_and_save_faces(input_image_dir, output_image_dir,
#                       flip_probability=flip_probability,
#                       brightness_range=brightness_range,
#                       scale_range=scale_range,
#                       num_augmentations=num_augmentations)


