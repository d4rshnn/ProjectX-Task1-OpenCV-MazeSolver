import cv2

image = cv2.imread("cleaned_maze.png")

row = 10

for col in range(0, 200):
    if (image[row, col] == [0, 0, 255]).all():
        print(col, "RED")
    else:
        print(col, "WHITE")