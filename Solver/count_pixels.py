import cv2
import numpy as np

image = cv2.imread("cleaned_maze.png")

red_pixels = np.sum(
    (image[:,:,0] == 0) &
    (image[:,:,1] == 0) &
    (image[:,:,2] == 255)
)

white_pixels = np.sum(
    (image[:,:,0] == 255) &
    (image[:,:,1] == 255) &
    (image[:,:,2] == 255)
)

print("Red pixels:", red_pixels)
print("White pixels:", white_pixels)
print("Total pixels:", red_pixels + white_pixels)