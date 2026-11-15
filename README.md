# 👁️ AI Object Detection & Direction Estimation

A real-time AI-powered object detection system built with **Python, YOLO-World, and OpenCV**.

The application detects objects through a webcam, identifies their labels, displays confidence scores, and estimates their direction relative to the camera's optical center using yaw and pitch angles.

## ✨ Features

- 🎯 Real-time object detection using YOLO-World
- 🌍 Open-vocabulary object recognition
- 📦 Bounding boxes around detected objects
- 📊 Detection confidence scores
- 🧭 Camera-relative direction estimation
- 📐 Yaw and pitch angle calculations
- ➡️ Direction arrows from camera center to detected objects
- 📷 Live webcam processing
- 📄 Custom object classes through `classes.txt`
- ⚡ Adjustable detection confidence and IoU thresholds

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| YOLO-World | Open-vocabulary object detection |
| OpenCV | Webcam access and visualization |
| NumPy | Numerical operations |
| Math | Angle and direction calculations |

## 📦 Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
```

**2. Install dependencies**

```bash
pip install ultralytics opencv-python numpy
```

**3. Download the YOLO-World model**

The application uses:

```text
yolov8s-worldv2.pt
```

The Ultralytics model loader can download the model automatically when it is not already available locally.

## 🚀 Usage

Run the application:

```bash
python main.py
```

Make sure your webcam is connected and accessible.

The application will start detecting objects and displaying their positions and estimated directions in real time.

Press `ESC` to exit.

## 🧭 Direction Estimation

The system calculates the horizontal and vertical angular position of each detected object relative to the camera's optical center.

**Yaw angle (horizontal direction):**

```python
yaw = math.degrees(math.atan2(ox - cx, fx))
```

**Pitch angle (vertical direction):**

```python
pitch = math.degrees(math.atan2(oy - cy, fy))
```

Where:

- `ox`, `oy` = Center coordinates of the detected object
- `cx`, `cy` = Camera optical center
- `fx`, `fy` = Approximate focal lengths in pixels

**Direction interpretation:**

| Angle | Direction |
|---|---|
| Positive yaw | Right |
| Negative yaw | Left |
| Positive pitch | Down |
| Negative pitch | Up |

*Note: These are approximate angular estimates based on an assumed focal length, not calibrated measurements.*

## ⚙️ Custom Object Classes

You can provide your own object labels through a file named `classes.txt`.

Example:

```text
person
car
dog
cat
laptop
mobile phone
chair
bottle
keyboard
backpack
```

Place the file in the same directory as `main.py`.

If `classes.txt` is missing, the application uses its built-in default object list.

## 🎛️ Detection Configuration

The detection settings can be modified inside the Python script:

```python
conf=0.25
iou=0.45
max_det=6000
```

| Parameter | Description |
|---|---|
| `conf` | Minimum confidence threshold |
| `iou` | Intersection over Union threshold |
| `max_det` | Maximum number of detections per image |

## 📁 Project Structure

```text
AI-OBJECT-DETECTION/
│
├── main.py
├── classes.txt
├── yolov8s-worldv2.pt
└── README.md
```

`classes.txt` and the model file are optional to include in the repository, depending on your setup. Avoid committing large model weights unnecessarily.

## ⚠️ Limitations

- Detection accuracy depends on lighting, camera quality, and model performance.
- Direction estimates depend on the assumed camera focal length.
- The system does not calculate actual object distance.
- Processing speed depends on available hardware.
- The number of detections does not guarantee recognition of every object in the camera view.

## 👨‍💻 Author

**Karan Kousik**

GitHub: [@cynox321-oss](https://github.com/cynox321-oss)

---

⭐ If you find this project interesting, consider giving it a star!

*Built with Python, computer vision, and AI.*
