import cv2
from gaze_tracking import GazeTracking
import numpy as np
import matplotlib.pyplot as plt

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

    # cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    # cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    # cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    # cv2.putText(frame, "Blink ct:  " + str(blink), (90, 200), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    # cv2.putText(frame, "Right ct: " + str(right), (90, 235), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    # cv2.putText(frame, "Left ct:  " + str(left), (90, 270), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    # cv2.putText(frame, "Center ct: " + str(center), (90, 305), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    # cv2.imshow("Demo", frame)
    return text,blink,right,left,center,left_pupil,right_pupil

# blink=0
# right=0
# left=0
# center=0

# left_pupil_coordinates = []
# right_pupil_coordinates = []

# webcam = cv2.VideoCapture(0)

# while True:
#     _, frame = webcam.read()
#     text,blink,right,left,center,left_pupil,right_pupil=gazetrack(blink,right,left,center,frame)
#     print(text)
#     if left_pupil != None and right_pupil != None:
#         left_pupil_coordinates.append((left_pupil[0], left_pupil[1]))
#         right_pupil_coordinates.append((right_pupil[0], right_pupil[1]))
#         cv2.circle(frame, (left_pupil[0], left_pupil[1]), 5, (0, 0, 255), -1)
#         cv2.circle(frame, (right_pupil[0], right_pupil[1]), 5, (0, 255, 0), -1)
#     cv2.imshow('Eye Tracking', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#             break


# left_pupil_coordinates = np.array(left_pupil_coordinates)
# right_pupil_coordinates = np.array(right_pupil_coordinates)

# # Generate a heatmap for the left and right pupil coordinates
# heatmap_left, xedges_left, yedges_left = np.histogram2d(left_pupil_coordinates[:, 1], left_pupil_coordinates[:, 0], bins=50)
# heatmap_right, xedges_right, yedges_right = np.histogram2d(right_pupil_coordinates[:, 1], right_pupil_coordinates[:, 0], bins=50)

# # Create a meshgrid from the histogram bin edges
# X_left, Y_left = np.meshgrid(xedges_left, yedges_left)
# X_right, Y_right = np.meshgrid(xedges_right, yedges_right)

# # Plot the left pupil heatmap
# plt.figure()
# plt.imshow(heatmap_left.T, origin='lower', extent=[xedges_left[0], xedges_left[-1], yedges_left[0], yedges_left[-1]])
# plt.colorbar()
# plt.title('Left Pupil Heatmap')
# plt.xlabel('X Coordinate')
# plt.ylabel('Y Coordinate')
# plt.show()

# # Plot the right pupil heatmap
# plt.figure()
# plt.imshow(heatmap_right.T, origin='lower', extent=[xedges_right[0], xedges_right[-1], yedges_right[0], yedges_right[-1]])
# plt.colorbar()
# plt.title('Right Pupil Heatmap')
# plt.xlabel('X Coordinate')
# plt.ylabel('Y Coordinate')
# plt.show()

# webcam.release()
# cv2.destroyAllWindows()        
# tot=blink+right+left+center
# blinkp=(blink/tot)*100
# rightp=(right/tot)*100
# leftp=(left/tot)*100
# centerp=(center/tot)*100
# # text_file = open(chosentxt, "w")
# # text_file.write(my_text_box.get(1.0, END))
# # text_file.close()

# with open("output.txt","w+") as file:
#     file.write(f'You spent { str(blinkp)} % of your ride blinking \n')
#     file.write(f'You spent { str(rightp)} % of your ride looking at the right \n')
#     file.write(f'You spent { str(leftp)} % of your ride looking at the left \n')
#     file.write(f'You spent { str(centerp)} % of your ride looking at the center \n')
#     print(str(blinkp))
# #file.close()