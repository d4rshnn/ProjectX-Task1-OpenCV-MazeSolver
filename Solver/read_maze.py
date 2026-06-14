import cv2
import numpy as np

image = cv2.imread("original_maze.png")

pixels = image.reshape(-1, 3)

unique_colors = np.unique(pixels, axis=0)

print("Number of unique colors:", len(unique_colors))

print(unique_colors)