import cv2
import os
from collections import deque

MOD = 1000000007
final_product = 1

os.makedirs("answers", exist_ok=True)

maze_files = sorted(os.listdir("mazes"))

print("Found", len(maze_files), "mazes")

impossible_image = cv2.imread("impossible.png")

for maze_name in maze_files:

    print("Processing:", maze_name)

    image = cv2.imread(f"mazes/{maze_name}")

    if image is None:
        print("Failed:", maze_name)
        continue

    cleaned = image.copy()

    mask = (
        (cleaned[:, :, 0] <= 100) &
        (cleaned[:, :, 1] <= 100) &
        (cleaned[:, :, 2] <= 100)
    )

    cleaned[mask] = [255, 255, 255]

    maze = []

    for row in range(40):

        maze_row = []

        for col in range(40):

            cell = cleaned[
                row * 20:(row + 1) * 20,
                col * 20:(col + 1) * 20
            ]

            red_pixels = (
                (cell[:, :, 0] == 0) &
                (cell[:, :, 1] == 0) &
                (cell[:, :, 2] == 255)
            ).sum()

            if red_pixels > 200:
                maze_row.append(1)
            else:
                maze_row.append(0)

        maze.append(maze_row)

    start = (0, 0)
    goal = (39, 39)

    queue = deque([start])

    visited = {start}

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

    path = []

    if found:

        current = goal

        while current != start:
            path.append(current)
            current = parent[current]

        path.append(start)

        path.reverse()

        path_length = len(path)

        print("Path length:", path_length)

        final_product = (final_product * path_length) % MOD

        for row, col in path:

            top = row * 20
            left = col * 20

            cleaned[
                top:top + 20,
                left:left + 20
            ] = [0, 255, 0]

        output_image = cleaned

    else:

        print("IMPOSSIBLE")

        output_image = impossible_image

    output_path = f"answers/{maze_name}"

    cv2.imwrite(output_path, output_image)

    print("Saved:", output_path)

with open("password.txt", "w") as f:
    f.write(str(final_product))

print()
print("FINAL PASSWORD =", final_product)
print("password.txt created")
print("DONE")