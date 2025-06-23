Python Face Blur Filter
A Python application that provides real-time face blurring capabilities with two distinct modes: picture processing and live webcam filtering.
Features

Picture Mode: Load and blur faces in static images with adjustable blur intensity
Live Mode: Real-time face blurring using your webcam
Adjustable Blur Level: Fine-tune the blur intensity from 0-100%
Face Detection Visualization: Optional bounding boxes and confidence scores
Fallback Detection: Maintains blur even when face detection temporarily fails in live mode

Prerequisites

Python 3.7 or higher
A webcam (for live mode)
Compatible operating system (Windows, macOS, Linux)

Installation

Clone the repository:
bashgit clone https://github.com/Quabbelig/Python_Face_Blur_Filter.git
cd Python_Face_Blur_Filter

Install required dependencies:
bashpip install -r requirements.txt


Usage
Starting the Application
Run the main script to launch the mode selection interface:
bashpython main.py
Picture Mode

Click "Blur Picture" in the main interface
Select an image file (supports .jpg, .jpeg, .png, .bmp)
Adjust the blur level using the slider (0-100%)
Toggle detection boxes to see face detection confidence
Click "Done" when satisfied with the preview
Choose to save the blurred image or go back to make adjustments

Live Mode

Click "Blur Live (Webcam)" in the main interface
Adjust blur intensity in real-time using the slider
Toggle detection boxes to visualize face detection
Press ESC to exit live mode

Important Notes for Live Mode
Camera Setup

Ensure your desired camera is connected to your PC before starting live mode
Set your camera to the highest priority in your system's camera settings
Multiple cameras: Make sure the one you want to use is set as the default/primary camera

First-Time Setup

Initial run may fail due to camera permission requests
If the program closes immediately when starting live mode, simply run it again
The camera permission dialog may cause a timeout on the first attempt
Subsequent runs should work normally once permissions are granted

Performance Tips

Close other applications that might be using your camera
Ensure good lighting for better face detection accuracy
The application uses fallback detection to maintain blur even when faces are temporarily not detected

Controls
Picture Mode

Slider: Adjust blur intensity (0-100%)
Checkbox: Show/hide detection boxes and confidence scores
Done: Finalize settings and proceed to save options
Back: Return to adjustment mode
Save: Export the blurred image
Exit: Close the application

Live Mode

Slider: Real-time blur intensity adjustment
Checkbox: Toggle detection visualization
ESC Key: Exit live mode

Technical Details

Face Detection: Uses CVZone's FaceDetectionModule for robust face detection
Blur Algorithm: OpenCV's blur function with adjustable kernel size
GUI Framework: Tkinter for the user interface
Video Processing: OpenCV for camera input and image processing

Troubleshooting
Common Issues

"Could not open webcam" error:

Check if your camera is properly connected
Ensure no other applications are using the camera
Try running the application as administrator


Program closes immediately in live mode:

This is normal on first run due to camera permissions
Simply restart the application


Poor face detection:

Ensure adequate lighting
Position your face clearly in the camera view
The application includes fallback detection for temporary detection failures


Installation issues:

Make sure you have Python 3.7+ installed
Try upgrading pip: pip install --upgrade pip
Install dependencies individually if batch installation fails



Dependencies
The application requires the following Python packages:

opencv-python
cvzone
tkinter (usually included with Python)

System Requirements

Python: 3.7 or higher
RAM: 4GB minimum (8GB recommended for smooth performance)
Camera: Any USB webcam or built-in camera
OS: Windows 10+, macOS 10.14+, or Linux with GUI support

Contributing
Feel free to fork this repository and submit pull requests for improvements or bug fixes.
License
This project is open source. Please check the repository for license details.
