import cv2
import argparse

from ultralytics import YOLO
import supervision as sv
import numpy as np


ZONE_POLYGON = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1]
])


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution", 
        default=[1280, 720], 
        nargs=2, 
        type=int
    )
    args = parser.parse_args()
    return args


def main(frame):
        result = model(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_yolov8(result)
        detections=detections[detections.class_id==0]
        
        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections
        )
        count_text = f"People Count: {len(detections)}"
        cv2.putText(frame, count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
<<<<<<< HEAD

=======
        
>>>>>>> 54c9ea68873745510750df9bb401ad624e0abaab
        zone.trigger(detections=detections)
        frame = zone_annotator.annotate(scene=frame)      
        
        cv2.imshow("yolov8", frame)
        return len(detections)
<<<<<<< HEAD
        

=======
>>>>>>> 54c9ea68873745510750df9bb401ad624e0abaab

if __name__ == "__main__":
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO("yolov8l.pt")

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )

    zone_polygon = (ZONE_POLYGON * np.array(args.webcam_resolution)).astype(int)
    zone = sv.PolygonZone(polygon=zone_polygon, frame_resolution_wh=tuple(args.webcam_resolution))
    zone_annotator = sv.PolygonZoneAnnotator(
        zone=zone, 
        color=sv.Color.red(),
        thickness=2,
        text_thickness=4,
        text_scale=2
    )
    while True:
        ret, frame = cap.read()
        peoplecount = main(frame)
        print(peoplecount)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break