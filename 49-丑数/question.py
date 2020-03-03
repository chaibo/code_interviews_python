"""
题目：我们把只包含因子 2、3 和 5 的数称作丑数(Ugly Number)。
求按从小到大的顺序的第 1500 个丑数。例如，6、8 都是丑数，但 14 不是，因为它包含因子 7。
习惯上我们把 1 当作第一个丑数。
"""


def get_ugly_number(index):
    if index <= 0:
        return 0

    ugly_numbers = [1]

    next_index = 1

    mul2 = mul3 = mul5 = 0

    while next_index < index:
        min_num = min(ugly_numbers[mul2] * 2,
                      ugly_numbers[mul3] * 3,
                      ugly_numbers[mul5] * 5)

        ugly_numbers.append(min_num)

        while ugly_numbers[mul2] * 2 <= ugly_numbers[next_index]:
            mul2 += 1
        while ugly_numbers[mul3] * 3 <= ugly_numbers[next_index]:
            mul3 += 1
        while ugly_numbers[mul5] * 5 <= ugly_numbers[next_index]:
            mul5 += 1

        next_index += 1

    return ugly_numbers[next_index - 1]


def test():
    index1 = -1
    index2 = 0
    index3 = 1
    index4 = 2
    index5 = 3
    index6 = 4
    index7 = 1500

    print("第 {} 个丑数是: {}".format(index1, get_ugly_number(index1)))
    print("第 {} 个丑数是: {}".format(index2, get_ugly_number(index2)))
    print("第 {} 个丑数是: {}".format(index3, get_ugly_number(index3)))
    print("第 {} 个丑数是: {}".format(index4, get_ugly_number(index4)))
    print("第 {} 个丑数是: {}".format(index5, get_ugly_number(index5)))
    print("第 {} 个丑数是: {}".format(index6, get_ugly_number(index6)))
    print("第 {} 个丑数是: {}".format(index7, get_ugly_number(index7)))


if __name__ == '__main__':
    test()
