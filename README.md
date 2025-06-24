#  Python Face Blur Filter

A Python application that provides real-time face blurring capabilities with two distinct modes: picture processing and live webcam filtering.

##  Features

- ** Picture Mode**: Load and blur faces in static images with adjustable blur intensity
- ** Live Mode**: Real-time face blurring using your webcam
- ** Adjustable Blur Level**: Fine-tune the blur intensity from 0-100%
- ** Face Detection Visualization**: Optional bounding boxes and confidence scores
- ** Fallback Detection**: Maintains blur even when face detection temporarily fails in live mode

##  Prerequisites

- Python version 3.12 or higher (lower versions can work, but there's a high chance that there will be bugs. (I used 3.12))
- A webcam (for live mode)
- Compatible operating system (Windows, macOS, Linux)

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
2. Select an image file ((supports `.jpg`, `.jpeg`, `.png`, `.bmp`)(make shure that the Image has a high enough reselution))
3. Adjust the blur level using the slider (0-100%)
4. If interested, toggle detection boxes to see face detection and confidence
5. Click **"Done"** when satisfied with the preview
6. Choose to save the blurred image, exit without saving or go back to make adjustments

### Live Mode

1. Click **"Blur Live (Webcam)"** in the main interface
2. Adjust the blur level using the slider (0-100%)
3. If interested, toggle detection boxes to see face detection and confidence
4. Press **ESC** to exit live mode

## Important Notes for Live Mode

### Camera Setup
- **Ensure your desired camera is connected** to your PC before starting live mode
- **Set your camera to the highest priority** in your system's camera settings, so that if you have multiple cameras or camera emulation softwares, the one you want to use is set as the default/primary camera

### First-Time Setup
- **Initial run may fail** due to camera permission requests
- Subsequent runs should work normally once permissions are granted

### Performance Tips
- Close other applications that might be using your camera
- Ensure good lighting for better face detection accuracy
- The application uses fallback detection to maintain blur even when faces are temporarily not detected

## Controls

### Picture Mode
- **Slider**: Adjust blur intensity (0-100%)
- **Checkbox**: Show/hide detection boxes and confidence scores
- **Done**: Finalize settings and proceed to save options
- **Back**: Return to adjustment mode
- **Save**: Export the blurred image
- **Exit**: Close the application

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

2. **Program closes immediately in live mode:**
   - This is normal on first run due to camera permissions
   - Simply restart the application

3. **Poor face detection:**
   - Ensure adequate lighting
   - Position your face clearly in the camera view
   - The application includes fallback detection for temporary detection failures

4. **Installation issues:**
   - Make sure you have Python 3.7+ installed
   - Try upgrading pip:
   ```bash
   pip install --upgrade pip
   ```
   - Install dependencies individually if batch installation fails

## Dependencies

The application requires the following Python packages:
- `opencv-python`
- `cvzone`
- `tkinter` (usually included with Python)

## System Requirements

- **Python**: 3.12 or higher (lower versions can work, but there's a high chance that there will be bugs. (I used 3.12))
- **RAM**: 4GB minimum (8GB recommended for smooth performance).
- **Camera**: Any camera, just has to have a decent resolution.
- **OS**: Windows 10+, macOS 10.14+, or Linux with GUI support.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes.

## License

This project is open source. Please check the repository for license details.

## If anyones interested in how I made it:

- [Entwicklungsprozess](./Entwicklungsprozess.md)
