import cv2

image = cv2.imread("cleaned_maze.png")

for row in [10, 30, 50, 70, 90]:
    for col in [10, 30, 50, 70, 90]:
        print(f"({row},{col}) =", image[row, col])