"""
题目：给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 "a"，
1 翻译成 "b"， ......， 11 翻译成 "l"，......，25 翻译成 "z"。
一个数字可能有多个翻译。例如，12258 有 5 种不同的翻译，分别是 "bccfi"、
"bwfi"、"bczi"、"mcfi" 和 "mzi"。请编程实现一个函数，用来计算一个数字
有多少种不同的翻译方法。
"""


def get_trans_count(num):
    if num < 0:
        return 0

    num_array = list(str(num))

    length = len(num_array)

    counts = [0] * length

    for i in range(length - 1, -1, -1):
        count = 0

        if i < length - 1:
            count = counts[i + 1]
        else:
            count = 1

        if i < length - 1:
            digit1 = int(num_array[i])
            digit2 = int(num_array[i + 1])
            number = digit1 * 10 + digit2

            if 10 <= number <= 25:
                if i < length - 2:
                    count += counts[i + 2]
                else:
                    count += 1

        counts[i] = count

    return counts[0]

def test():
    num1 = -1
    num2 = 0
    num3 = 1
    num4 = 5
    num5 = 25
    num6 = 26
    num7 = 12258
    num8 = 12345234324

    print("{} 有 {} 种不同的翻译方法".format(num1, get_trans_count(num1)))
    print("{} 有 {} 种不同的翻译方法".format(num2, get_trans_count(num2)))
    print("{} 有 {} 种不同的翻译方法".format(num3, get_trans_count(num3)))
    print("{} 有 {} 种不同的翻译方法".format(num4, get_trans_count(num4)))
    print("{} 有 {} 种不同的翻译方法".format(num5, get_trans_count(num5)))
    print("{} 有 {} 种不同的翻译方法".format(num6, get_trans_count(num6)))
    print("{} 有 {} 种不同的翻译方法".format(num7, get_trans_count(num7)))
    print("{} 有 {} 种不同的翻译方法".format(num8, get_trans_count(num8)))

if __name__ == '__main__':
    test()
