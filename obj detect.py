# pip install ultralytics opencv-python numpy

import cv2
import math
import numpy as np
from ultralytics import YOLOWorld

# Load open-vocabulary model (can handle many classes)
model = YOLOWorld("yolov8s-worldv2.pt")   # use yolov8l-worldv2.pt for better accuracy

# Load class names from classes.txt (put 5053+ class names here, one per line)
try:
    with open("classes.txt", "r", encoding="utf-8") as f:
        class_names = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    # Default small list if classes.txt is missing
    class_names = [
        "person", "car", "dog", "cat", "chair", "table", "bottle",
        "laptop", "phone", "book", "cup", "keyboard", "mouse",
        "backpack", "umbrella", "traffic light", "stop sign",
        "bench", "fire hydrant", "bicycle"
    ]

model.set_classes(class_names)

# Open camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise SystemExit("Cannot open camera")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    cx, cy = w / 2.0, h / 2.0          # camera optical axis center
    fx = fy = w * 1.2                  # approximate focal length in pixels

    # Detect many objects per frame
    results = model.predict(
        frame,
        conf=0.25,
        iou=0.45,
        max_det=6000,                  # allows >5053 detections
        verbose=False
    )
    result = results[0]

    # Draw camera optical axis center
    cv2.drawMarker(frame, (int(cx), int(cy)), (0, 255, 255),
                   cv2.MARKER_CROSS, 20, 2)

    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
        cls_id = int(box.cls[0])
        label = class_names[cls_id] if cls_id < len(class_names) else f"obj{cls_id}"
        conf = float(box.conf[0])

        # Object center
        ox = (x1 + x2) / 2.0
        oy = (y1 + y2) / 2.0

        # Direction relative to camera optical axis
        yaw = math.degrees(math.atan2(ox - cx, fx))     # + right, - left
        pitch = math.degrees(math.atan2(oy - cy, fy))   # + down,  - up

        # Draw box, center, direction arrow, and text
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.circle(frame, (int(ox), int(oy)), 4, (0, 0, 255), -1)
        cv2.arrowedLine(frame, (int(cx), int(cy)), (int(ox), int(oy)),
                        (255, 0, 0), 2, tipLength=0.05)
        cv2.putText(
            frame,
            f"{label} {conf:.2f} yaw:{yaw:.1f} pitch:{pitch:.1f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )

    cv2.imshow("Object Detection + Camera-Axis Direction", frame)
    if cv2.waitKey(1) & 0xFF == 27:   # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()