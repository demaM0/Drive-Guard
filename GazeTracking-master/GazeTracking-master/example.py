import cv2
from gaze_tracking import GazeTracking
import numpy as np
from heatmap import Heatmap

def gazetrack(blink,right,left,center,frame):

    gaze = GazeTracking()

    # We send this frame to GazeTracking to analyze it

    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
        blink+=1
    elif gaze.is_right():
        text = "Looking right"
        right+=1
    elif gaze.is_left():
        text = "Looking left"
        left+=1
    elif gaze.is_center():
        text = "Looking center"
        center+=1

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.putText(frame, "Blink ct:  " + str(blink), (90, 200), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right ct: " + str(right), (90, 235), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Left ct:  " + str(left), (90, 270), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Center ct: " + str(center), (90, 305), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.imshow("Demo", frame)
    return text,blink,right,left,center,left_pupil,right_pupil

blink=0
right=0
left=0
center=0
heatmap = Heatmap()
heatmap_canvas = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
left_pupil_coordinates = []
right_pupil_coordinates = []

webcam = cv2.VideoCapture(0)

while True:
    _, frame = webcam.read()
    text,blink,right,left,center,left_pupil,right_pupil=gazetrack(blink,right,left,center,frame)
    print(text)
    left_pupil_coordinates.append((left_pupil[0], left_pupil[1]))
    right_pupil_coordinates.append((right_pupil[0], right_pupil[1]))
    cv2.circle(frame, (left_pupil[0], left_pupil[1]), 5, (0, 0, 255), -1)
    cv2.circle(frame, (right_pupil[0], right_pupil[1]), 5, (0, 255, 0), -1)
    heatmap_canvas = heatmap.update(heatmap_canvas, left_pupil_coordinates, opacity=0.5, intensity=1.0)
    heatmap_canvas = heatmap.update(heatmap_canvas, right_pupil_coordinates, opacity=0.5, intensity=1.0)
    cv2.imshow('Eye Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

heatmap_image = heatmap.generate(heatmap_canvas)
cv2.imshow('Eye Tracking Heatmap', heatmap_image)
cv2.waitKey(0)

webcam.release()
cv2.destroyAllWindows()