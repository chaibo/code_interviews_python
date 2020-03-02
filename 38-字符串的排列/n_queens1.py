"""
题目：在 N*N 的国际象棋上摆放 N 个皇后，使其不能相互攻击，
即任意两个皇后不得处在同一行、同一列或者同一条对角线上。
"""

"""
使用Python 生成器的解法。
"""

def conflict(state, next_x):
    next_y = len(state)
    for i in range(next_y):
        if abs(state[i] - next_x) in (0, next_y - i):
            return True
    return False


def queens(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield pos,
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def pretty_print(solution):
    def line(pos, length=len(solution)):
        return '. ' * pos + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


if __name__ == '__main__':
    n = 8
    for s in queens(8):
        pretty_print(s)
        print('-' * 15)