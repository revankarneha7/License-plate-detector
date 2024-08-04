# Number Plate Detection and OCR

This project is a Python application for detecting number plates in images and videos, processing the detected plates using OpenCV, and extracting text from the plates using Tesseract OCR. The detected text is then logged and saved into a CSV file.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.6 or higher
- Tesseract OCR
- OpenCV
- Tkinter

## Installation

### Tesseract OCR

Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract). Ensure the executable is added to your system PATH.

### Python Dependencies

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/number-plate-detection.git
    cd number-plate-detection
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Detecting Number Plates in Images

1. Run the script:
    ```sh
    python main.py -u
    ```

2. A file dialog will appear allowing you to select an image file. The script will process the image, detect any number plates, extract text, and display the results.

### Detecting Number Plates in Video

1. Run the script:
    ```sh
    python main.py -v
    ```

2. The script will start capturing video from your webcam, detect any number plates, extract text, and display the results in real-time. Press 's' to save a detected plate image and 'q' to quit.

### Running the Test Scripts

1. To test the image upload functionality:
    ```sh
    python scripts/upload_image.py
    ```

2. To test the video detection functionality:
    ```sh
    python scripts/video_detection.py
    ```

## Project Structure

```plaintext
number-plate-detection/
│
├── model/
│   └── haarcascade_russian_plate_number.xml   # Haar Cascade XML file for number plate detection
│
├── logs/
│   ├── number_plate_detection.log             # Log file (auto-generated)
│   └── data.csv                               # CSV file to store detected text (auto-generated)
│
├── plates/                                    # Directory to save detected plate images (auto-generated)
│
├── module/
│   ├── config.py                              # Configuration file for paths and Tesseract settings
│   ├── utils.py                               # Utility functions for text extraction and saving data
│   ├── video_detection.py                     # Module for detecting number plates in video
│   └── image_upload_detection.py              # Module for detecting number plates in images
│
├── scripts/
│   ├── upload_image.py                        # Script for testing image upload detection
│   └── video_detection.py                     # Script for testing video detection
│
├── main.py                                    # Main application script
├── requirements.txt                           # Python dependencies
├── README.md                                  # Project documentation
└── .gitignore                                 # Git ignore file
