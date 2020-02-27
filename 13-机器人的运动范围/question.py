"""
题目：地上有一个 m 行 n 列的方格。一个机器人从坐标(0, 0)的格子开始移动，它每次可以向左、右、
上、下移动一格，但不能进入行坐标和列坐标的数位之和大于 k 的格子。例如，当 k 为 18 时，机器人
能够进入方格(35, 37)，因为 3+5+3+7=18，但它不能进入方格(35, 38)，因为 3+5+3+8=19。请问
该机器人能够到达多少个格子？
"""

# 回溯法
def moving_count(threshold, rows, cols):
    if (threshold < 0) or (rows <= 0) or (cols <= 0):
        return 0

    visited = [False] * rows * cols

    count = moving_count_core(threshold, rows, cols, 0, 0, visited)

    return count

def moving_count_core(threshold, rows, cols, row, col, visited):
    count = 0
    if check(threshold, rows, cols, row, col, visited):
        visited[row * cols + col] = True

        count = 1 + moving_count_core(threshold, rows, cols,
                                      row - 1, col, visited) \
                + moving_count_core(threshold, rows, cols,
                                    row + 1, col, visited) \
                + moving_count_core(threshold, rows, cols,
                                    row, col - 1, visited) + \
                moving_count_core(threshold, rows, cols,
                                  row, col + 1, visited)

    return count

def check(threshold, rows, cols, row, col, visited):
    if (0 <= row < rows) and (0 <= col < cols) \
            and (not visited[row * cols + col]) \
            and (digit_sum(row) + digit_sum(col) <= threshold):
        return True

    return False

def digit_sum(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10

    return sum


print(moving_count(5, 4, 6))
print(moving_count(3, 1, 4))
print(moving_count(2, 4, 1))


# 本题的非回溯法
def moving_count2(threshold, rows, cols):
    if (threshold < 0) or (rows <= 0) or (cols <= 0):
        return 0

    count = 0
    for row in range(rows):
        for col in range(cols):
            if (digit_sum(row) + digit_sum(col)) <= threshold:
                count += 1

    return count

print(moving_count2(5, 4, 6))
print(moving_count2(3, 1, 4))
print(moving_count2(2, 4, 1))
