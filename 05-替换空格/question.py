"""
题目：请实现一个函数，把字符串中的每个空格替换成"%20"。
例如，输入"We are happy."，则输出"We%20are%20happy."。
"""

def replace_blank(str, str_len, arr_len):
    """
    对字符数组原地修改。
    :param str: 包含原始字符串的数组
    :param str_len: 字符串长度
    :param arr_len: 数组总容量
    """
    if (str is None) or (str_len <= 0) or (arr_len <= 0) or (str_len > arr_len):
        print("输入无效。")
        return

    # 统计字符串中的空格
    num_of_blank = 0

    for i in range(str_len):
        if str[i] == ' ':
            num_of_blank += 1

    new_len = str_len + num_of_blank * 2
    if new_len > arr_len:
        print("数组容量不足")
        return

    index_of_orignial = str_len - 1
    index_of_new = new_len - 1

    while (index_of_orignial >= 0) and (index_of_new > index_of_orignial) :
        if str[index_of_orignial] == ' ':
            str[index_of_new-2 : index_of_new+1] = "%20"
            index_of_new -= 3
        else:
            str[index_of_new] = str[index_of_orignial]
            index_of_new -= 1

        index_of_orignial -= 1


test_case1 = list("we are happy.") + [None] * 10
print(test_case1)
replace_blank(test_case1, 13, 23)
print(test_case1)

test_case2 = list(" we are happy.") + [None] * 10
print(test_case2)
replace_blank(test_case2, 14, 24)
print(test_case2)

test_case3 = list(" we are happy. ") + [None] * 10
print(test_case3)
replace_blank(test_case3, 15, 25)
print(test_case3)

test_case4 = list("wearehappy.") + [None] * 10
print(test_case4)
replace_blank(test_case4, 11, 21)
print(test_case4)

test_case5 = None
print(test_case5)
replace_blank(test_case5, 0, 0)
print(test_case5)


