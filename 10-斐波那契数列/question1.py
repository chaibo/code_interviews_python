"""
题目：写一个函数，输入n，求斐波那契(Fibonacci)数列的第 n 项。
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)  n>1
"""

# 递归
def fib1(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fib1(n-1) + fib1(n-2)


# 循环
def fib2(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    fib1 = 0
    fib2 = 1
    fib_n = 0
    for i in range(2, n+1):
        fib_n = fib1 + fib2
        fib1 = fib2
        fib2 = fib_n

    return fib_n

print(fib1(10))
print(fib2(10))
