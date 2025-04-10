# Real-Time Invisibility Cloak

This project creates a real-time invisibility cloak effect using Python and OpenCV. The effect works by detecting a red-colored cloth and replacing it with the background in real-time.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## How to Use

1. Run the script:
```bash
python invisibility_cloak.py
```

2. When the program starts:
   - Stand in front of your webcam
   - Hold a red-colored cloth in front of you
   - The program will capture the background for 3 seconds
   - After that, move the red cloth around to create the invisibility effect

3. To exit the program, press 'q' on your keyboard.

## Tips for Best Results

- Use a bright red cloth for better detection
- Ensure good lighting conditions
- Keep the background static for the best effect
- Avoid wearing red clothes while using the cloak
- Make sure the red cloth covers the area you want to make invisible

## How it Works

1. The program captures the background when it starts
2. It detects red color in the video feed using HSV color space
3. Creates a mask of the red-colored areas
4. Replaces the red areas with the corresponding background
5. Displays the result in real-time

## Note

The effectiveness of the invisibility cloak depends on:
- Lighting conditions
- The shade of red used
- Camera quality
- Background stability 