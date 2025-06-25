#  Python Face Blur Filter

A Python application that provides real-time face blurring capabilities with two distinct modes: picture processing and live webcam filtering.

##  Features

- ** Picture Mode**: Load and blur faces in static images with adjustable blur intensity
- ** Live Mode**: Real-time face blurring using your webcam
- ** Adjustable Blur Level**: Fine-tune the blur intensity from 0-100%
- ** Face Detection Visualization**: Optional bounding boxes and confidence scores
- ** Fallback Detection**: Maintains blur even when face detection temporarily fails in live mode

##  Prerequisites

- **Python**: 3.12 or higher (older versions may cause bugs, but I didn't test it. (I used 3.12)).
- **RAM**: 4GB minimum (8GB recommended for smooth performance).
- **Camera**: Any camera (has to have a decent resolution.)
- **OS**: Windows 10+, macOS 10.14+, or Linux with GUI support.

## Dependencies

The application requires the following Python packages:
- `opencv-python`
- `cvzone`
- `tkinter` (usually included with Python)

##  Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Quabbelig/Python_Face_Blur_Filter.git
cd Python_Face_Blur_Filter
```

2. **Install required dependencies:**
```bash
pip install -r requirements.txt
```

##  Usage

### Starting the Application

Run the main script to launch the mode selection interface:

```bash
python main.py
```

### Picture Mode

1. Click **"Blur Picture"** in the main interface
2. Select an image file ((supports `.jpg`, `.jpeg`, `.png`, `.bmp`)(make shure that the image has a decent reselution))
3. Adjust the blur level using the **"Slider"** or the **"Box"** (0-100%)
4. If interested, toggle the **"Show detection box and confidence"** box to show detection box and confidence level.
5. Click **"Done"** when satisfied with the preview
6. Click **"Save"** to save the blurred image, **"Exit"** to exit without saving or **"Back"** to go back to make adjustments

### Live Mode

1. Click **"Blur Live (Webcam)"** in the main interface
3. Adjust the blur level using the **"Slider"** or the **"Box"** (0-100%)
4. If interested, toggle the **"Show detection box and confidence"** box to show detection box and confidence level.
5. Press your **"esc"** button to exit live mode

## Important Notes for Live Mode

### Camera Setup
- **Ensure your desired camera is connected** to your PC before starting live mode
- **Set your camera to the highest priority** in your system's camera settings, so that if you have multiple cameras or camera emulation software, the one you want to use is set as the default/primary camera

### First-Time Setup
- **Initial run may fail** due to camera permission requests
- Subsequent runs should work normally once permissions are granted

### Performance Tips
- Close other applications that might be using your camera

## Controls

### Picture Mode
- **Slider**: Adjust blur intensity (0-100%)
- **Checkbox**: Show/hide detection boxes and confidence scores
- **Done**: Finalize settings and proceed to save options
- **Back**: Return to adjustment mode
- **Save**: Save the blurred image
- **Exit**: Close the application without saving

### Live Mode
- **Slider**: Adjust blur intensity (0-100%)
- **Checkbox**: Show/hide detection boxes and confidence scores
- **ESC Key**: Exit live mode

## Technical Details

- **Face Detection**: Uses CVZone's FaceDetectionModule for robust face detection
- **Blur Algorithm**: OpenCV's blur function with adjustable kernel size
- **GUI Framework**: Tkinter for the user interface
- **Video Processing**: OpenCV for camera input and image processing

## Troubleshooting

### Common Issues

1. **"Could not open webcam" error:**
   - Check if your camera is properly connected
   - Ensure no other applications are using the camera
   - Try running the application as administrator
   - This is normal on first run due to camera permissions (simply run it again, after granting Permission)

2. **Program closes immediately, without any error in live mode:**
   - This is normal on first run due to camera permissions (simply run it again, after granting Permission)

3. **Poor face detection:**
   - Ensure decent Picture/Camera resolution.
   - Ensure decent lighting in Picture/Room.
   - Ensure that Face/Faces are clearly in frame.

5. **Installation issues:**
   - Make sure you have Python 3.12 or higher (older versions may cause bugs, but I didn't test it. (I used 3.12)).
   - Try upgrading pip:
   ```bash
   pip install --upgrade pip
   ```
   - Install dependencies individually if batch installation fails

## Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes.

## License

This project is open source. Please check the repository for license details.

## If anyone's interested in how I made it:

- [Entwicklungsprozess](./Entwicklungsprozess.md)
