"""
题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。例如输入字符串 "I am a student."，
则输出 "student. a am I"。
"""


def reverse_sentence(string):
    if not string:
        return string

    str_list = list(string)
    length = len(str_list)

    reverse(str_list, 0, length - 1)

    start = end = 0

    while start < length:
        if str_list[start] == ' ':
            start += 1
            end += 1
        elif (end == length) or (str_list[end] == ' '):
            reverse(str_list, start, end - 1)
            end += 1
            start = end
        else:
            end += 1

    return ''.join(str_list)


def reverse(array, start, end):
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1


def test():
    str1 = None
    str2 = ''
    str3 = '  '
    str4 = 'student'
    str5 = 'I am a student.'

    print("{} 翻转结果为 {}".format(repr(str1), repr(reverse_sentence(str1))))
    print("{} 翻转结果为 {}".format(repr(str2), repr(reverse_sentence(str2))))
    print("{} 翻转结果为 {}".format(repr(str3), repr(reverse_sentence(str3))))
    print("{} 翻转结果为 {}".format(repr(str4), repr(reverse_sentence(str4))))
    print("{} 翻转结果为 {}".format(repr(str5), repr(reverse_sentence(str5))))


if __name__ == '__main__':
    test()
