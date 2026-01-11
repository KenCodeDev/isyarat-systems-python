# Isyarat Systems

**Isyarat Systems** is a Python program that functions as a real-time **hand gesture detection system** using a camera. This program can:

* Detect hands and faces using MediaPipe.
* Identify finger poses to determine specific gestures.
* Automatically display subtitles based on detected gestures.
* Speak subtitles using *gTTS-based text-to-speech (TTS)**.
* Provide a visual display with highlights, subtitles, FPS, and author name.
* Adjust camera brightness and contrast.

This program is suitable for gesture-based interaction demonstrations, education, presentations, or multimedia projects.

---

## ✨ Main Features

* **Hand Gesture Recognition** (MediaPipe Hands)
* **Face Detection** (MediaPipe Face Detection)
* **Auto Subtitle Rendering**
* **Text-to-Speech** with gTTS + pygame
* **Real-time Overlay Display** (OpenCV)
* **Gesture Mapping to Text**
* **Auto Clean TTS Cache**
* **Multi-line Text Subtitle Support**

---

## 👤 Author

This program was created by:

**Kenichi Ichi**

---

## 📚 Libraries Used

This program uses several Python libraries:

* **OpenCV (cv2)** — for the camera and overlay display
* **MediaPipe** — for hand and face detection
* **NumPy** — for array operations
* **gTTS** — for Text-to-Speech (Google Text-to-Speech)
* **pygame** — to play the TTS audio file
* **threading** — to ensure TTS runs without interrupting the camera process
* **time** — delay and timing
* **random** — generate temporary TTS file names
* **os** — temporary TTS file management
* **colorsys** (in tobgr.py) — convert HSL/HSV colors to RGB/BGR

---

## 🐍 Supported Python Versions

> **Requires Python version 3.9 to 3.11**

If using a version **below 3.9** or **above 3.11**, some libraries such as MediaPipe or pygame may cause errors or fail to install.

---

## 📄 Additional Files: tobgr.py

This file converts various color formats such as:

* RGB
* HEX
* HSL
* HSV

to the **BGR** format, which is used by OpenCV.

---

## 🔧 How to Run the Program

1. Make sure you are using **Python 3.9 - 3.11**
2. Install the required libraries:
Note : Do not use MediaPipe other than version 0.10.21
```bash
pip install opencv-python mediapipe==0.10.21 pygame gTTS numpy
```

*

3. Run the program:

```bash
py main.py
```
or
```bash
python main.py
```

---

## ❗ Note

* The program will automatically create and delete temporary TTS files.
* Press **Q** or **ESC** to exit.
* The "Isyarat Systems" window is resizable.
* Gesture mapping is in the `detect_gesture()` function.
* Do not use MediaPipe other than version 0.10.21

---

## ❤️ Thank you for using Igu Systems!
