"""
题目：用两个队列实现一个栈。
"""

from queue import Queue

queue1 = Queue()
queue2 = Queue()

# 入栈
def push(value):
    if not queue2.empty():
        queue2.put(value)
    else:
        queue1.put(value)

# 出栈
def pop():

    if not queue1.empty():
        while True:
            item = queue1.get(block=False)
            if not queue1.empty():
                queue2.put(item)
            else:
                return item

    if not queue2.empty():
        while True:
            item = queue2.get(block=False)
            if not queue2.empty():
                queue1.put(item)
            else:
                return item

    return None

print(pop())
push(1)
push(2)
push(3)
push(4)
print(pop())
print(pop())
print(pop())
push(5)
print(pop())
print(pop())
print(pop())



