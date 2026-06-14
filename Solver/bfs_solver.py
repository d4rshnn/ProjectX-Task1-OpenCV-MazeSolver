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

# for row in maze:
#    print(row)

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
        (row - 1, col),  # up
        (row + 1, col),  # down
        (row, col - 1),  # left
        (row, col + 1)   # right
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

if found:    
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    print("Path length:", len(path))
    print("Path:", path)