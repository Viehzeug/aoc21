import numpy as np


with open('input.txt', 'r') as f:
    lines = f.readlines()
    max_x = max_y = 0
    geo_lines = []
    for line in lines:
        x1, y1, x2, y2 = line.replace(' -> ', ',').split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)
        geo_lines.append((x1, y1, x2, y2))

grid = np.zeros((max_x + 1, max_y + 1))
for x1, y1, x2, y2 in geo_lines:
    if x1 == x2 or y1 == y2: #horizontal or vertical
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        grid[x1:(x2+1), y1:(y2+1)] += 1
cnt = (grid >= 2).sum()
print('Task 1:', cnt)


grid = np.zeros((max_x + 1, max_y + 1))
for x1, y1, x2, y2 in geo_lines:
    if x1 == x2 or y1 == y2: #horizontal or vertical
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        grid[x1:(x2+1), y1:(y2+1)] += 1
    elif (k := abs(x1 - x2)) == abs(y1 - y2): #diagonal
        dx = np.sign(x2 - x1)
        dy = np.sign(y2 - y1)
        for j in range(k+1):
            grid[x1+j*dx, y1+j*dy] += 1
cnt = (grid >= 2).sum()
print('Task 2:', cnt)


