"""
题目：队列的最大值。
请定义一个队列并实现函数 max 得到队列里的最大值， 要求函数
max、push_back、pop_front 的时间复杂度为O(1)。
"""

from collections import deque


class QueueItem:
    def __init__(self, value, index):
        self.value = value
        self.index = index


class QueueWithMax:

    def __init__(self):
        self.data = deque()
        self.max_num = deque()
        self.cur_index = 0

    def push_back(self, num):
        while self.max_num and (num > self.max_num[-1].value):
            self.max_num.pop()

        item = QueueItem(num, self.cur_index)
        self.data.append(item)
        self.max_num.append(item)

        self.cur_index += 1

    def pop_front(self):
        if not self.max_num:
            raise Exception("Queue is empty.")

        if self.max_num[0].index == self.data[0].index:
            self.max_num.popleft()

        return self.data.popleft().value

    def max(self):
        if not self.max_num:
            raise Exception("Queue is empty.")

        return self.max_num[0].value


def test():
    test_queue = QueueWithMax()

    while True:
        num = input("Please a num, g for pop, q for quit: ")
        if num == "q":
            break
        elif num == "g":
            print("出队列: {}".format(test_queue.pop_front()))
            print("队列最大值为: {}".format(test_queue.max()))
        else:
            test_queue.push_back(int(num))
            print("队列最大值为: {}".format(test_queue.max()))


if __name__ == '__main__':
    test()
