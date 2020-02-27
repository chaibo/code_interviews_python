"""
题目：给你一根长度为 n 的绳子，请把绳子剪成 m 段(m、n都是整数，n>1 并且 m>1)，每段绳子
的长度记为 k[0],k[1],...,k[m]。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，
当绳子的长度是 8 时，我们把它剪成长度分别为 2、3、3 的三段，此时得到的最大乘积为 18。
"""

"""
动态规划
f(n) = max[f(i)*f(n-i)]  0 < i <n
"""

def max_product1(length):
    if length < 2:
        return 0

    if length == 2:    # 因为需要剪开，所以为1*1
        return 1

    if length == 3:    # 因为需要剪开，所以为1*2
        return 2

    products = [0, 1, 2, 3]

    for i in range(4, length + 1):
        max = 0
        for j in range(1, (i // 2) + 1):
            product = products[j] * products[i - j]
            if max < product:
                max = product

        products.append(max)

    return products[length]


"""
贪婪算法
当n>=5 时，我们尽可能多地剪长度为3的绳子；
当剩下的绳子长度为4时，把绳子剪成两段长度为2的绳子。
"""
def max_product2(length):
    if length < 2:
        return 0

    if length == 2:
        return 1

    if length == 3:
        return 2

    # 尽可能多的剪去长度为3的绳子段
    time_of3 = length // 3

    # 当绳子最后剩下的长度为4的时候，不能再剪去长度为3的绳子段
    # 此时更好的方法是把绳子剪成长度为2的两段，因为2*2 > 3*1
    if (length - time_of3 * 3) == 1:
        time_of3 -= 1

    time_of2 = (length - time_of3 * 3) // 2

    return pow(3, time_of3) * pow(2, time_of2)

print(max_product1(0))
print(max_product1(1))
print(max_product1(2))
print(max_product1(3))
print(max_product1(4))
print(max_product1(5))
print(max_product1(8))
print()
print(max_product2(0))
print(max_product2(1))
print(max_product2(2))
print(max_product2(3))
print(max_product2(4))
print(max_product2(5))
print(max_product2(8))
