"""
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如，序列 {1, 2, 3, 4, 5} 是某栈的压栈序列，
序列 {4，5，3，2，1} 是该压栈序列对应的一个弹出序列，但 {4, 3, 5, 1, 2}
就不可能是该压栈序列的弹出序列。
"""


def is_pop_order(push_l, pop_l):
    is_order = False

    if (push_l is not None) and (pop_l is not None) \
            and (len(push_l) == len(pop_l)) and (len(push_l) >= 0):

        length = len(push_l)
        next_push = 0
        next_pop = 0
        stack = []

        while next_pop < length:
            while (len(stack) == 0) or (stack[-1] != pop_l[next_pop]):
                if next_push == length:
                    break

                stack.append(push_l[next_push])
                next_push += 1

            if stack[-1] != pop_l[next_pop]:
                break

            stack.pop()

            next_pop += 1

        if (len(stack) == 0) and (next_push == length):
            is_order = True

    return is_order


def test():
    push1 = [1, 2, 3, 4, 5]
    pop1 = [4, 5, 3, 2, 1]
    print("压入序列: {}, 弹出序列: {}, 判断结果: {}"
          .format(push1, pop1, is_pop_order(push1, pop1)))

    pop2 = [4, 3, 5, 1, 2]
    print("压入序列: {}, 弹出序列: {}, 判断结果: {}"
          .format(push1, pop2, is_pop_order(push1, pop2)))

    push2 = [1]
    pop3 = [1]
    pop4 = [2]

    print("压入序列: {}, 弹出序列: {}, 判断结果: {}"
          .format(push2, pop3, is_pop_order(push2, pop3)))
    print("压入序列: {}, 弹出序列: {}, 判断结果: {}"
          .format(push2, pop4, is_pop_order(push2, pop4)))

    print("压入序列: {}, 弹出序列: {}, 判断结果: {}"
          .format(None, None, is_pop_order(None, None)))


if __name__ == '__main__':
    test()
