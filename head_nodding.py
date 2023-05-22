import cv2
import mediapipe as mp
from onedollar import TrajectoryClasification, OneDollarRecognizer

def headturn():
    # Number of frames to skip before adding nose point to the list
    FRAME_SKIP = 70
    head_tracker = TrajectoryClasification(OneDollarRecognizer())

    # Initialize Mediapipe face detection and landmark models
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    mp_face_mesh = mp.solutions.face_mesh

    # Initialize variables
    frame_count = 0
    type_of_movement = None
    confidence = 0

    # Start capturing video from default camera
    cap = cv2.VideoCapture(0)

    # Initialize face detection and landmark models
    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection, \
            mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:

        while True:
            # Read a frame from the video capture
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the BGR frame to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame with face detection
            results_detection = face_detection.process(frame_rgb)

            # Check if any faces are detected
            if results_detection.detections:
                for detection in results_detection.detections:
                    # Extract the face landmarks
                    face_landmarks = face_mesh.process(frame_rgb)

                    # Check if face landmarks are available
                    if face_landmarks.multi_face_landmarks:
                        for face_landmark in face_landmarks.multi_face_landmarks:
                            # Draw the face landmarks on the frame
                            mp_drawing.draw_landmarks(
                                frame, face_landmark, mp_face_mesh.FACEMESH_CONTOURS)

                            # Extract the nose landmark (landmark index 4)
                            nose_landmark = face_landmark.landmark[4]
                            nose_x = int(nose_landmark.x * frame.shape[1])
                            nose_y = int(nose_landmark.y * frame.shape[0])

                            # Append the nose point to the list every 70 frames
                            frame_count += 1
                            head_tracker.append_to_list((nose_x, nose_y))
                            if frame_count % FRAME_SKIP == 0:
                                # Call dollarpy
                                type_of_movement, confidence = head_tracker.trajectoryType()
                                head_tracker.resetPoints()
            if type_of_movement == "yes" and confidence>0.4:
                cv2.putText(frame, "Turn off alarm YES", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
                return "yes"
            if type_of_movement == "no" and confidence>0.5:
                cv2.putText(frame, "NO", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
                return "no"
            cv2.putText(frame, "Type of movement: " + str(type_of_movement) + " Confidence: " + str(confidence), (10, 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))

            # Show the frame with landmarks
            cv2.imshow('Facial Landmarks', frame)

            # Exit the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the video capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

