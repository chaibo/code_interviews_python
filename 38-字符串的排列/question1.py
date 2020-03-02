"""
题目：输入一个字符串，打印出该字符串中字符的所有排列。
例如，输入字符串 abc，则打印出由字符 a, b, c 所能排列出的所有字符串
abc、acb、bac、bca、cab 和 cba。
"""


def permutation(string):
    if not string:
        return

    char_list = list(string)
    permutation_core(char_list, 0)


def permutation_core(char_list, index):
    length = len(char_list)

    if index == length:
        string = ''.join(char_list)
        print(string)
    else:
        for i in range(index, length):
            temp = char_list[i]
            char_list[i] = char_list[index]
            char_list[index] = temp

            permutation_core(char_list, index + 1)

            temp = char_list[i]
            char_list[i] = char_list[index]
            char_list[index] = temp


def test():
    test_case1 = "a"
    test_case2 = "abc"
    test_case3 = ""
    test_case4 = None

    print("字符串 {} 中的字符排列: ".format(test_case1))
    permutation(test_case1)
    print("字符串 {} 中的字符排列: ".format(test_case2))
    permutation(test_case2)
    print("字符串 {} 中的字符排列: ".format(test_case3))
    permutation(test_case3)
    print("字符串 {} 中的字符排列: ".format(test_case4))
    permutation(test_case4)


if __name__ == '__main__':
    test()
