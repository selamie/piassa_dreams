import cv2
import os
import random
import time
import numpy as np

# Paths for images and videos
image_paths = [
    'images/image_2.png',
    'images/image_3.png',
    'images/image_4.png',
    'images/image_6.png',
    'images/image_7.png',
    'images/image_8.png',
    'images/image_9.png',
    'images/image_10.png',
]

video_paths = [
    'videos/generated_2.mp4',
    'videos/generated_3.mp4',
    'videos/generated_4.mp4',
    'videos/generated_6.mp4',
    'videos/generated_7.mp4',
    'videos/generated_8.mp4',
    'videos/generated_9.mp4',
    'videos/generated_10.mp4'
]

# Function to display an image in a window
def display_image(image_path):
    image = cv2.imread(image_path)
    cv2.imshow("Gallery", image)
    cv2.waitKey(0)

# Function to play a video
def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Gallery", frame)
        # Wait for 20ms or break on keypress
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cap.release()

# Main function to cycle through images and videos
def main():
    cv2.namedWindow("Gallery", cv2.WINDOW_NORMAL)

    while True:
        # Pick a random image to display
        image_path = random.choice(image_paths)
        display_image(image_path)
        
        # Randomly decide if we should replace it with a video
        if random.random() < 0.3:  # 30% chance to replace with video
            video_path = random.choice(video_paths)
            play_video(video_path)

        # Random wait time between switching images or videos
        time.sleep(random.uniform(0.5, 1))  # Random time between 2 to 7 seconds

        # To stop the loop manually
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
