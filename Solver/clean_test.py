import cv2
import numpy as np

image = cv2.imread("X task 1 Windows/mazes/maze_01.png")

cleaned = image.copy()

mask = (
    (cleaned[:,:,0] <= 100) &
    (cleaned[:,:,1] <= 100) &
    (cleaned[:,:,2] <= 100)
)

cleaned[mask] = [255,255,255]

cv2.imwrite("cleaned_maze.png", cleaned)

print("Saved cleaned_maze.png")