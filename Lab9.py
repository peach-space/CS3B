#################################################
# Lab 9
# Student Name: Cen Li
#################################################

from collections import deque


def numSquares(n):
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1

    queue = deque([(n, 0)])
    visited = {n}

    while queue:
        remainder, count = queue.popleft()

        for square in squares:
            next_val = remainder - square

            if next_val == 0:
                return count + 1

            if next_val > 0 and next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, count + 1))

    return count


# test
print(numSquares(12))  # output:3
print(numSquares(13))  # output:2