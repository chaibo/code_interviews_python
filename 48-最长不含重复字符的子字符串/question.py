"""
题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
假设字符串中只包含 'a'~'z' 的字符。例如，在字符串 "arabcacfr" 中，最长的不含重
复字符的子字符串是 "acfr"，长度为4。
"""


def longest_substr(string):
    if not string:
        return 0

    cur_len = 0
    max_len = 0
    length = len(string)

    char_pos = [-1] * 26

    for i in range(length):

        pre_pos = char_pos[ord(string[i]) - 97]

        if (pre_pos < 0) or ((i - pre_pos) > cur_len):
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len

            cur_len = i - pre_pos

        char_pos[ord(string[i]) - 97] = i

    if cur_len > max_len:
        max_len = cur_len

    return max_len


def test():
    str1 = None
    str2 = ""
    str3 = "a"
    str4 = "abcdefg"
    str5 = "arabcacfr"
    str6 = "aaaaa"

    print("字符串 {} 的最长不重复子字符串的长度为: {}".format(repr(str1),
                                             longest_substr(str1)))
    print("字符串 {} 的最长不重复子字符串的长度为: {}".format(repr(str2),
                                             longest_substr(str2)))
    print("字符串 {} 的最长不重复子字符串的长度为: {}".format(repr(str3),
                                             longest_substr(str3)))
    print("字符串 {} 的最长不重复子字符串的长度为: {}".format(repr(str4),
                                             longest_substr(str4)))
    print("字符串 {} 的最长不重复子字符串的长度为: {}".format(repr(str5),
                                             longest_substr(str5)))
    print("字符串 {} 的最长不重复子字符串的长度为: {}".format(repr(str6),
                                             longest_substr(str6)))


if __name__ == '__main__':
    test()
