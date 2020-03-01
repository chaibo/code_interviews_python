"""
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数。
在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
"""


class Stack:
    """
    包含 min 函数的栈。
    用列表模拟栈。
    """

    def __init__(self):
        # 数据栈
        self.data_stack = []
        # 辅助栈
        self.min_stack = []

    def push(self, value):
        self.data_stack.append(value)

        if (len(self.min_stack) == 0) or (self.min_stack[-1] > value):
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):

        value = None

        if (len(self.data_stack) > 0) and (len(self.min_stack) > 0):
            value = self.data_stack.pop()
            self.min_stack.pop()

        return value

    def min(self):

        if (len(self.data_stack) > 0) and (len(self.min_stack) > 0):
            return self.min_stack[-1]

        return None


def test():
    test_stack = Stack()
    test_stack.push(3)
    print("压入3后，栈的最小值为: {}".format(test_stack.min()))
    test_stack.push(4)
    print("压入4后，栈的最小值为: {}".format(test_stack.min()))
    test_stack.push(2)
    print("压入2后，栈的最小值为: {}".format(test_stack.min()))
    test_stack.push(1)
    print("压入1后，栈的最小值为: {}".format(test_stack.min()))
    test_stack.pop()
    print("弹出栈顶元素后，栈的最小值为: {}".format(test_stack.min()))
    test_stack.pop()
    print("弹出栈顶元素后，栈的最小值为: {}".format(test_stack.min()))
    test_stack.push(0)
    print("压入0后，栈的最小值为: {}".format(test_stack.min()))


if __name__ == '__main__':
    test()
