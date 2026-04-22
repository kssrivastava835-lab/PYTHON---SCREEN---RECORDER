# PYTHON---SCREEN---RECORDER
A lightweight Python-based screen recorder that captures real-time screen activity using OpenCV and PyAutoGUI, saves recordings in MP4 format, and includes automatic window minimization using Win32 APIs 
- Python Screen Recorder

A lightweight and efficient **screen recording tool built using Python**, capable of capturing real-time screen activity and saving it as a video file. This project combines **computer vision, automation, and system-level control** to deliver a simple yet functional screen recorder.

 Features

*  Real-time screen recording (1920x1080 resolution)
* Saves recordings in `.mp4` format using XVID codec
* Automatically minimizes the recording window to avoid obstruction
*  Simple keyboard control (`q` to stop recording)
*  Automatically creates a `recordings/` folder to store output files
*  Timestamp-based file naming for unique recordings



##  Tech Stack

* **OpenCV** – Video writing and frame processing
* **PyAutoGUI** – Screen capture
* **NumPy** – Frame conversion and array handling
* **Win32 APIs** – Window minimization (Windows-specific)
* **Time & OS modules** – File handling and naming



##  How It Works

1. The script continuously captures screenshots using PyAutoGUI.
2. Each screenshot is converted into a NumPy array.
3. Frames are processed using OpenCV (RGB → BGR conversion).
4. Processed frames are written into a video file using `cv2.VideoWriter`.
5. The recording window is minimized automatically after launch.
6. Press **`q`** to stop recording and save the file.


* Press **`q`** → Stop recording
- Autor : Kshitj Srivastava

