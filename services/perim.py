import numpy as np

matrix = np.zeros((5, 3))
matrix[0, 0] = 255
matrix[1, 0] = 255
matrix[0, 1] = 255
matrix[-1, -1] = 255
matrix[-1, -2] = 255
matrix[2, 2] = 100
shape = [5, 3]
visited = np.zeros((5, 3))

i = 0
j = 0

print(matrix)


def perimeter_walk(matrix, shape, visited, i, j):
    boundary = {(i, j)}
    colour = matrix[i, j]
    start_i = i
    start_j = j
    # we consider the first pixel was entered from the right
    # so we backtrack left
    p_i = start_i
    p_j = start_j
    # we consider the first pixel was entered from the right
    # so we backtrack left
    c_i = p_i
    c_j = p_j - 1
    c_i -= 1
    # since we backtracked left, the first direction to look is up (clockwise rotation)
    direction = 1  # 0 is left, 1 is up, 2 is right, 3 is down
    while True:
        print('boundary', boundary)
        print(c_i, c_j)
        if c_i == start_i and c_j == start_j and direction == 2:
            break
        # colour matches and inside the matrix
        if matrix[c_i, c_j] == colour and c_i > -1 and c_j > -1:
            boundary.add((c_i, c_j))
            p_i = c_i
            p_j = c_j
            print('backtrack!')
            if direction == 0:  # if left backtrack right
                c_j += 1
                direction = 2
            elif direction == 1:  # if up backtrack down
                c_i += 1
                direction = 3
            elif direction == 2:  # if right backtrack left
                c_j -= 1
                direction = 0
            elif direction == 3:  # if down backtrack up
                c_i -= 1
                direction = 1
        else:
            direction = (direction + 1) % 4  # rotate direction clockwise
            if direction == 0:
                c_j -= 1
            elif direction == 1:
                c_i -= 1
            elif direction == 2:
                c_j += 1
            elif direction == 3:
                c_i += 1
    return boundary


print(perimeter_walk(matrix, shape, visited, i, j))
