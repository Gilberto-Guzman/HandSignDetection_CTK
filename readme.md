# HandSignDetection
### Hi teacher, Next I will provide you with the corresponding work to deliver:

## Code.

Código: https://github.com/Gilberto-Guzman/HandSignDetection

## Teach Video.

https://www.youtube.com/watch?v=0X9li2Ge1QQ

# Documentation.

## The following tools/libraries were used to carry out this project:

## Interpreter
- python 3.7

## Libraries
- cvzone 1.5.6
- mediapipe 0.9.1.0
- opencv-python 4.5.4.60
- tensorflow 2.9.1

## Cloud Server
- teachable machine

# Explanation of the code:

## datacollection.py

The code imports some modules like cv2, numpy, math, time and HandDetector from the cvzone library. It then initializes the camera by capturing a VideoCapture object with index 0 (the default camera) and a hand detector with a maximum detection limit of one hand.

Some variables such as offset, imgSize and folder are defined. The while loop runs indefinitely and on each iteration, one frame is read from the camera and the hand is detected using the hand detector.

If a hand is detected, the bounding box enclosing the hand is computed. A blank image of the size specified by imgSize is created, and the cropped image of the hand is scaled to have the same aspect ratio as the blank image.

If the aspect ratio of the cropped image is greater than 1, it means that the image is taller than it is wide. Therefore, the cropped image is resized to have a height of imgSize and the width is adjusted to maintain the original aspect ratio. If the aspect ratio is less than 1, the reverse is done.

The resized image is placed in the center of the blank image. The cropped image and the blank image are displayed in separate windows. If the "s" key is pressed, the blank image is saved to the folder specified by folder with a unique file name based on the current time. The counter is incremented by one and is displayed on the screen.

## test.py

This is a Python script that uses the OpenCV library to capture video images from the computer's camera, detect a hand, and predict the letter displayed on the palm of the hand.

The code imports several Python modules, including cv2, numpy, and math, and also imports two specific modules for hand detection and image classification, called HandDetector and Classifier, respectively.

Next, a HandDetector instance is initialized to detect a hand in each video frame, and a Classifier instance is initialized to predict the letter displayed on the palm of the hand.

Then, a number of variables are defined, including offset, imgSize, and folder. These variables are used to resize and crop the images of the hand.

The code then goes into an infinite while loop that continuously captures video frames from the camera and processes the image to detect the hand and predict the handwriting.

In the loop, each video frame is read and detector.findHands() is called to find the hand in the image. If a hand is detected, the image is cropped and resized to fit the desired size, and classifier.getPrediction() is called to predict the letter displayed on the palm of the hand.

Finally, boxes are drawn around the hand and the rendered image is displayed in an OpenCV window. The loop continues until the user presses the 'q' key to exit the program.

