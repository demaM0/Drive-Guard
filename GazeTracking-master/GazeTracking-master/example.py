import cv2
from gaze_tracking import GazeTracking
def gaze(frame,blink,right,left,center):

    gaze = GazeTracking()

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
    return blink,right,left,center, text

webcam = cv2.VideoCapture(0)
blink=0
right=0
left=0
center=0
while True:
    _, frame = webcam.read()
    blink,right,left,center,direction = gaze(frame,blink,right,left,center)
    print(direction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
webcam.release()
cv2.destroyAllWindows()