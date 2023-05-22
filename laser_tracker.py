import cv2
import numpy as np
def laser_tracker(frame):
    #cap = cv2.VideoCapture(0)
    #while True:
    # Read a frame from the video source
    #ret, frame = cap.read()

    #if not ret:
    #   break

    # Convert the frame to the HSV color space for easier color filtering
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper thresholds for the red color range
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Create a mask to filter out the red color in the frame
    mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # Find contours of the red objects in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any contours are detected
    if len(contours) > 0:
        # Get the largest contour (assuming the red point is the largest)
        largest_contour = max(contours, key=cv2.contourArea)

        # Get the bounding rectangle coordinates for the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Calculate the center point of the bounding rectangle
        center_x = x + (w // 2)
        center_y = y + (h // 2)

        # Check the position of the center point relative to the screen width
        screen_width = frame.shape[1]
        if center_x < screen_width // 2:
            text = "Left"
            #return "steering left"
        else:
            text = "Right"
            #return "steering right"

        # Draw the center point and text on the frame
    #     cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
    #     cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    #
    # # Display the frame
    # cv2.imshow("Frame", frame)

    # Exit the loop if the 'q' key is pressed
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    # Release the video capture object and close any windows
    # cap.release()
    # cv2.destroyAllWindows()
