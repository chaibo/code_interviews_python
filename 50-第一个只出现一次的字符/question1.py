"""
题目：字符串中第一个只出现一次的字符。
在字符串中找出第一个只出现一次的字符。如输入 "abaccdeff"，则输出 "b"。
"""


def find_no_repeat_char(string):
    if not string:
        return None

    hash_table = [0] * 256

    for s in string:
        hash_table[ord(s)] += 1

    for s in string:
        if hash_table[ord(s)] == 1:
            return s

    return None


def test():
    s1 = None
    s2 = ""
    s3 = "abcdefg"
    s4 = "abaccdeff"
    s5 = "aabbccddfee"
    s6 = "aabbccddff"

    print("{} 中，第一次只出现一次的字符是: {}".format(repr(s1),
                                         find_no_repeat_char(s1)))
    print("{} 中，第一次只出现一次的字符是: {}".format(repr(s2),
                                         find_no_repeat_char(s2)))
    print("{} 中，第一次只出现一次的字符是: {}".format(repr(s3),
                                         find_no_repeat_char(s3)))
    print("{} 中，第一次只出现一次的字符是: {}".format(repr(s4),
                                         find_no_repeat_char(s4)))
    print("{} 中，第一次只出现一次的字符是: {}".format(repr(s5),
                                         find_no_repeat_char(s5)))
    print("{} 中，第一次只出现一次的字符是: {}".format(repr(s6),
                                         find_no_repeat_char(s6)))


if __name__ == '__main__':
    test()
