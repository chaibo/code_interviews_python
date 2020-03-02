"""
N 皇后，数组全排列解法。
对数组[0, 1, 2, 3, 4, 5, 6, 7]进行全排列。
"""


def n_queens(n):
    if n <= 0:
        return

    array = []

    for i in range(n):
        array.append(i)

    n_queens_core(array, n, 0)


def n_queens_core(array, n, index):

    if index == n:
        if not conflict(array, n):
            print("{}皇后解法之一：{}".format(n, array))
            print('-' * 15)
            pretty_print(array)
            print('-' * 15)

    else:
        for i in range(index, n):
            temp = array[i]
            array[i] = array[index]
            array[index] = temp

            n_queens_core(array, n, index + 1)

            temp = array[i]
            array[i] = array[index]
            array[index] = temp


def conflict(array, length):
    for i in range(length):
        for j in range(length):
            if (i != j) and (abs(i - j) == abs(array[i] - array[j])):
                return True

    return False


def pretty_print(solution):
    def line(pos, length=len(solution)):
        return '. ' * pos + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


if __name__ == '__main__':
    n = 8
    n_queens(n)
