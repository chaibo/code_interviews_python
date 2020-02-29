"""
题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串 "+100"、"5e2"、"-123"、"3.1416" 及 "-1E-16" 都表示数值，
但 "12e"、"1a3.14"、"1.2.3"、"+-5" 及 "12e+5.4" 都不是。
"""

"""
数字的格式可以用 A[.[B]][e|EC] 或者 .B[e|EC] 表示，
其中 A 和 C 都是整数 (可以有正负号，也可以没有)，而 B 是一个无符号整数。
"""

def is_num(string):
    if (string is None) or (len(string) <= 0):
        return False

    is_numeric = False

    length = len(string)
    pos = 0

    # 数字开头的正负号
    if (string[pos] == '+') or (string[pos] == '-'):
        pos += 1

    # 开头去掉正号或负号的整数部分
    new_pos = scan_unsigned_integer(string, length, pos)

    is_numeric = new_pos > pos
    pos = new_pos

    # 如果出现'.'，则接下来是小数部分
    if (pos < length) and (string[pos] == '.'):
        pos += 1
        new_pos = scan_unsigned_integer(string, length, pos)

        # 使用 or，原因如下：
        # 1. 小数可以没有整数部分，如 .123 等于 0.123；
        # 2. 小数点后面可以没有数字，如 233. 等于 233.0
        # 3. 小数点前面和后面都可以有数字，如 2.5
        is_numeric = (new_pos > pos) or is_numeric
        pos = new_pos

    # 如果出现 'e' 或者 'E'，则接下来是数字的指数部分
    if (pos < length) and ((string[pos] == 'e') or (string[pos] == 'E')):
        pos += 1
        if (pos < length) and ((string[pos] == '+') or (string[pos] == '-')):
            pos += 1

        new_pos = scan_unsigned_integer(string, length, pos)

        # 使用 and，原因如下：
        # 1. 当 e 或 E 前面没有数字时，整个字符串不能表示数字，如 .e1、e1；
        # 2. 当 e 或 E 后面没有整数时，整个字符串不能表示数字，如 12e、12e+5.4
        is_numeric = (new_pos > pos) and is_numeric
        pos = new_pos

    return (is_numeric and (pos >= length))


def scan_unsigned_integer(string, length, pos):
    while (pos < length) and (48 <= ord(string[pos]) <= 57):
        pos += 1

    return pos


print(is_num("+100"))
print(is_num("5e2"))
print(is_num("-123"))
print(is_num("3.1416"))
print(is_num("+e100"))
print(is_num("-1E-16"))
print(is_num("12e"))
print(is_num("1a3.14"))
print(is_num("1.2.3"))
print(is_num("+-5"))
print(is_num("12e+5.4"))
print(is_num(".123"))
print(is_num("123."))
print(is_num("5.4"))
print(is_num(".e1"))
print(is_num("e1"))
