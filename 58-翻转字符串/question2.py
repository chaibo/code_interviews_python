"""
题目：左旋转字符串。
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串 "abcdefg" 和数字 2，
该函数将返回左旋转两位得到的结果 "cdefgab"
"""


def reverse(array, start, end):
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1


def left_r_string(string, n):
    if string:
        str_l = list(string)
        length = len(str_l)
        if 0 < n < length:
            start1 = 0
            end1 = n - 1
            start2 = n
            end2 = length - 1

            reverse(str_l, start1, end1)
            reverse(str_l, start2, end2)
            reverse(str_l, start1, end2)

            string = ''.join(str_l)

    return string


def test():
    str1 = None
    str2 = ''
    str3 = 'abcdefg'

    print(" {} 左旋转 {} 个字符是 {}".format(repr(str1), 1,
                                      repr(left_r_string(str1, 1))))
    print(" {} 左旋转 {} 个字符是 {}".format(repr(str2), 1,
                                      repr(left_r_string(str2, 1))))
    print(" {} 左旋转 {} 个字符是 {}".format(repr(str3), -1,
                                      repr(left_r_string(str3, -1))))
    print(" {} 左旋转 {} 个字符是 {}".format(repr(str3), 0,
                                      repr(left_r_string(str3, 0))))
    print(" {} 左旋转 {} 个字符是 {}".format(repr(str3), 1,
                                      repr(left_r_string(str3, 1))))
    print(" {} 左旋转 {} 个字符是 {}".format(repr(str3), 2,
                                      repr(left_r_string(str3, 2))))
    print(" {} 左旋转 {} 个字符是 {}".format(repr(str3), 3,
                                      repr(left_r_string(str3, 3))))
    print(" {} 左旋转 {} 个字符是 {}".format(repr(str3), 4,
                                      repr(left_r_string(str3, 4))))
    print(" {} 左旋转 {} 个字符是 {}".format(repr(str3), 5,
                                      repr(left_r_string(str3, 5))))
    print(" {} 左旋转 {} 个字符是 {}".format(repr(str3), 6,
                                      repr(left_r_string(str3, 6))))
    print(" {} 左旋转 {} 个字符是 {}".format(repr(str3), 7,
                                      repr(left_r_string(str3, 7))))


if __name__ == '__main__':
    test()
