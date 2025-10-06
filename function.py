


# #import dependency
# import cv2
# import numpy as np
# import os
# import mediapipe as mp

# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_hands = mp.solutions.hands

# def mediapipe_detection(image, model):
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
#     image.flags.writeable = False                  # Image is no longer writeable
#     results = model.process(image)                 # Make prediction
#     image.flags.writeable = True                   # Image is now writeable 
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
#     return image, results

# def draw_styled_landmarks(image, results):
#     if results.multi_hand_landmarks:
#       for hand_landmarks in results.multi_hand_landmarks:
#         mp_drawing.draw_landmarks(
#             image,
#             hand_landmarks,
#             mp_hands.HAND_CONNECTIONS,
#             mp_drawing_styles.get_default_hand_landmarks_style(),
#             mp_drawing_styles.get_default_hand_connections_style())


# def extract_keypoints(results):
#     if results.multi_hand_landmarks:
#       for hand_landmarks in results.multi_hand_landmarks:
#         rh = np.array([[res.x, res.y, res.z] for res in hand_landmarks.landmark]).flatten() if hand_landmarks else np.zeros(21*3)
#         return(np.concatenate([rh]))
# # Path for exported data, numpy arrays
# DATA_PATH = os.path.join('MP_Data') 

# actions = np.array(['A','B','C'])

# no_sequences = 30

# sequence_length = 30


# # import cv2
# # import numpy as np
# # import os
# # from ultralytics import YOLO

# # # Load YOLO Pose model (lightweight)
# # model = YOLO("yolov8n-pose.pt")

# # # This replaces mediapipe_detection()
# # def mediapipe_detection(image, model_yolo):
# #     results = model_yolo(image)
# #     return image, results

# # # This replaces draw_styled_landmarks()
# # def draw_styled_landmarks(image, results):
# #     if results and len(results) > 0:
# #         annotated_image = results[0].plot()  # YOLO's built-in drawing
# #         return annotated_image
# #     return image

# # # This replaces extract_keypoints()
# # def extract_keypoints(results):
# #     if results and len(results) > 0 and results[0].keypoints is not None:
# #         # Shape: (num_persons, num_keypoints, 3)
# #         keypoints = results[0].keypoints.data.cpu().numpy()
# #         # Flatten the first detected person
# #         return keypoints[0].flatten()
# #     else:
# #         return np.zeros(17 * 3)  # YOLOv8 pose has 17 keypoints

# # # Path for exported data
# # DATA_PATH = os.path.join('MP_Data') 
# # actions = np.array(['S', 'R', 'F'])
# # no_sequences = 30
# # sequence_length = 30

# # # Webcam loop (example usage)
# # cap = cv2.VideoCapture(0)
# # while cap.isOpened():
# #     ret, frame = cap.read()
# #     if not ret:
# #         break

# #     image, results = mediapipe_detection(frame, model)
# #     image = draw_styled_landmarks(image, results)

# #     keypoints = extract_keypoints(results)
# #     print("Keypoints shape:", keypoints.shape)

# #     cv2.imshow("Hand Tracking", image)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# # cap.release()
# # cv2.destroyAllWindows()
