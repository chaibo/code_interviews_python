"""
题目：字符流中第一个只出现一次的字符。
请实现一个函数，用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个
字符 "go" 时，第一个只出现一次的字符是 "g"; 当从该字符流中读出前 6 个字符 "google"
时，第一个只出现一次的字符是 "l"。
"""


class CharStatistics:

    def __init__(self):
        self.hash_table = [-1] * 256
        self.index = 0

    def insert(self, char):
        if self.hash_table[ord(char)] == -1:
            self.hash_table[ord(char)] = self.index
        elif self.hash_table[ord(char)] >= 0:
            self.hash_table[ord(char)] = -2

        self.index += 1

    def first_appearing_once(self):
        char = None
        min_index = self.index + 1

        for i in range(256):
            if (self.hash_table[i] >= 0) and (self.hash_table[i] < min_index):
                char = chr(i)
                min_index = self.hash_table[i]

        return char


def test():
    char_statistics = CharStatistics()
    while True:
        ch = input("Please insert a char, Ctrl + C for quit: ")
        char_statistics.insert(ch)
        print("输入字符：{}".format(ch))
        print("第一次只出现一次的字符：{}"
              .format(char_statistics.first_appearing_once()))


if __name__ == '__main__':
    test()
