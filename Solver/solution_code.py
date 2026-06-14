import cv2

image = cv2.imread("X task 1 Windows/mazes/maze_01.png")

cleaned = image.copy()

mask = (
    (cleaned[:,:,0] <= 100) &
    (cleaned[:,:,1] <= 100) &
    (cleaned[:,:,2] <= 100)
)

cleaned[mask] = [255,255,255]

print("Cleaning complete")

maze = []

for row in range(40):

    maze_row = []

    for col in range(40):

        cell = cleaned[
            row*20:(row+1)*20,
            col*20:(col+1)*20
        ]

        red_pixels = (
            (cell[:,:,0] == 0) &
            (cell[:,:,1] == 0) &
            (cell[:,:,2] == 255)
        ).sum()

        if red_pixels > 200:
            maze_row.append(1)
        else:
            maze_row.append(0)

    maze.append(maze_row)

print("Maze extracted")
print("Start:", maze[0][0])
print("End:", maze[39][39])

from collections import deque

start = (0, 0)
goal = (39, 39)

queue = deque([start])

visited = set()
visited.add(start)

parent = {}

found = False

while queue:

    current = queue.popleft()

    if current == goal:
        found = True
        break

    row, col = current

    neighbors = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]

    for nr, nc in neighbors:

        if not (0 <= nr < 40 and 0 <= nc < 40):
            continue

        if maze[nr][nc] == 1:
            continue

        if (nr, nc) in visited:
            continue

        visited.add((nr, nc))

        parent[(nr, nc)] = current

        queue.append((nr, nc))

print("Goal found:", found)
print("Visited cells:", len(visited))

path = []

if found:

    current = goal

    while current != start:

        path.append(current)
        current = parent[current]

    path.append(start)

    path.reverse()

print("Path length:", len(path))

for row, col in path:

    top = row * 20
    left = col * 20

    cleaned[
        top:top+20,
        left:left+20
    ] = [0, 255, 0]

cv2.imwrite("solved_maze.png", cleaned)

print("Solved maze saved")