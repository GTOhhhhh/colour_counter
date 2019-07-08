import numpy as np

matrix = np.zeros((5, 3))
matrix[0, 0] = 255
matrix[1, 0] = 255
matrix[0, 1] = 255
matrix[-1, -1] = 255
matrix[-1, -2] = 255

print(matrix)

if direction == 'above':  # walk right
    for x in range(shape[0] - min_x - 1):
        max_x += 1
        if matrix[min_y, x] != colour:
            direction = 'right'
            continue
        print('min_x: ', min_x)
        print('min_y: ', min_y)
        print('max_x', max_x)
        print('max_ y:', max_y)

if direction == 'right':  # walk down
    for y in range(shape[1] - min_y - 1):
        print('elem: ', matrix[y, max_x])
        max_y += 1
        if matrix[y, max_x] != colour:
            direction = 'down'
            continue
        print('min_x: ', min_x)
        print('min_y: ', min_y)
        print('max_x', max_x)
        print('max_ y:', max_y)

if direction == 'down':  # walk left
    for x in range(shape[1] - min_y - 1):
        print('elem: ', matrix[y, max_x])
        max_y += 1
        if matrix[y, max_x] != colour:
            direction = 'down'
            continue
        print('min_x: ', min_x)
        print('min_y: ', min_y)
        print('max_x', max_x)
        print('max_ y:', max_y)

if pos == start:
    break


def flood_fill(output, matrix, visited, i, j):
    stack = deque()
    stack.append((i, j))
    while stack:
        curr = stack.pop()
        if visited[curr[0], curr[1]]:
            continue
        else:
            visited[curr[0], curr[1]] = 1
            try:

                north = matrix[(i - 1), j]
                stack.append((i - 1, j))
            except IndexError:
                'north out of range'
            try:
                south = matrix[i + 1, j]
                stack.append((i + 1, j))
            except IndexError:
                'north out of range'
            try:
                west = matrix[i, j - 1]
                stack.append((i, j + 1))
            except IndexError:
                'north out of range'
            try:
                east = matrix[i, j + 1]
                stack.append((i, j + 1))
            except IndexError:
                'north out of range'