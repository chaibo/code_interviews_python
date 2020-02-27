"""
题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一
条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的 3*4 的矩阵
中包含一条字符串 "bfce" 的路径，但矩阵中不包含字符串 "abfb" 的路径，因为字符串
的第一个字符 b 占据了矩阵中的第一行第二个格子后，路径不能再次进入这个格子。

a  b  t  g
c  f  c  s
j  d  e  h
"""

def has_path(matrix, rows, cols, string):

    if (matrix is None) or (rows < 1) or (cols < 1) \
            or (string is None):
        return False

    # 用来标识路径是否已经进入了每个格子的布尔值矩阵
    visited = [False] * rows * cols

    for row in range(rows):
        for col in range(cols):
            if has_path_core(matrix, rows, cols, row, col, string, 0, visited):
                return True

    return False

def has_path_core(matrix, rows, cols, row, col, string, path_len, visited):
    if path_len == len(string):
        return True

    has = False
    if (0 <= row <rows) and (0 <= col < cols) \
            and (matrix[row * cols + col] == string[path_len]) \
            and (not visited[row * cols + col]):

        path_len += 1
        visited[row * cols + col] = True

        has = has_path_core(matrix, rows, cols, row, col - 1,
                            string, path_len, visited) \
              or has_path_core(matrix, rows, cols, row, col + 1,
                               string, path_len, visited) \
              or has_path_core(matrix, rows, cols, row - 1, col,
                               string, path_len, visited) \
              or has_path_core(matrix, rows, cols, row + 1, col,
                               string, path_len, visited)

        if not has:
            visited[row * cols + col] = False

    return has


matrix1 = ["a", "b", "t", "g", "c", "f", "c", "s", "j", "d", "e", "h"]
print(has_path(matrix1, 3, 4, "bfce"))
print(has_path(matrix1, 3, 4, "abfb"))

matrix2 = ["a", "b", "c", "d"]
print(has_path(matrix2, 1, 4, "abcd"))
print(has_path(matrix2, 1, 4, "abcb"))
print(has_path(matrix2, 4, 1, "abcd"))
print(has_path(matrix2, 4, 1, "abcb"))

print(has_path(None, 4, 5, "sdfd"))


