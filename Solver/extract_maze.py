import cv2

image = cv2.imread("cleaned_maze.png")

maze = []

for row in range(40):

    maze_row = []

    for col in range(40):

        center_row = row * 20 + 10
        center_col = col * 20 + 10

        pixel = image[center_row, center_col]

        if (pixel == [0, 0, 255]).all():
            maze_row.append(1)   # wall
        else:
            maze_row.append(0)   # path

    maze.append(maze_row)

for row in maze:
    print(row)

print("Start:", maze[0][0])
print("End:", maze[39][39])