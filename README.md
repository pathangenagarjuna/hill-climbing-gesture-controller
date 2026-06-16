# Hill Climbing Gesture Controller

## Overview

A gesture-controlled gaming system that allows players to control Hill Climb Racing using body movements. The project uses real-time pose estimation to detect wrist positions and translate them into acceleration and braking actions.

This project showcases Human-Computer Interaction through Computer Vision.

## Features

* Real-time body tracking
* Gesture-based acceleration
* Gesture-based braking
* Webcam-controlled gameplay
* Interactive visual guidance
* Low-latency response

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyDirectInput

## Controls

| Gesture                | Action     |
| ---------------------- | ---------- |
| Hand Above Center Line | Accelerate |
| Hand Below Center Line | Brake      |

## How It Works

1. Webcam captures player movements.
2. MediaPipe detects body landmarks.
3. Wrist position is tracked.
4. Gestures are mapped to keyboard inputs.
5. Hill Climb Racing responds instantly.

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Project Structure

```text
hill-climbing-gesture-controller/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Future Improvements

* Multiple gesture controls
* Steering support
* Gesture customization
* Advanced game integration

## Author

Pathange Nagarjuna
