import cv2

image = cv2.imread("cleaned_maze.png")

for col in range(40):
    center_col = col * 20 + 10

    pixel = image[10, center_col]

    if (pixel == [0, 0, 255]).all():
        print("1", end="")
    else:
        print("0", end="")

print()