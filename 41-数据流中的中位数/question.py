import heapq

"""
题目：如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
"""

"""
使用Python heapq模块。
heapq模块实现了一个适用于Python列表的最小堆排序算法。
通过插入数值的相反数实现最大堆排序算法。
"""


class DynamicArray:
    """
    包含一个最大堆和一个最小堆。
    """

    def __init__(self):
        # 最小堆
        self.min = []
        # 最大堆
        self.max = []

    def insert(self, value):
        """
        插入数据
        """
        if (len(self.min) + len(self.max)) & 1 == 0:
            if (len(self.max) > 0) and (value < (- self.max[0])):
                heapq.heappush(self.max, - value)

                value = - self.max[0]

                heapq.heappop(self.max)

            heapq.heappush(self.min, value)
        else:
            if (len(self.min) > 0) and (value > self.min[0]):
                heapq.heappush(self.min, value)

                value = self.min[0]

                heapq.heappop(self.min)

            heapq.heappush(self.max, - value)

    def get_median(self):
        """
        获取已有所有数据的中位数
        """
        size = len(self.min) + len(self.max)
        if size == 0:
            raise Exception("No numbers are available")

        median = 0
        if size & 1 == 1:
            median = self.min[0]
        else:
            median = (self.min[0] + (- self.max[0])) / 2

        return median


def main():
    dynamic_array = DynamicArray()

    while True:
        value = input("Please insert a integer, input q for quit: ")
        if value == 'q':
            break

        num = int(value)

        print("Insert number: {}".format(num))
        dynamic_array.insert(num)
        print("The median number is: {}".format(dynamic_array.get_median()))


if __name__ == '__main__':
    main()
