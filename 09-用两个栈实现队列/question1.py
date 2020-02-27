"""
题目：用两个栈实现一个队列。分别实现在队列尾部插入节点和在队列头部删除节点的功能。
"""

# 用列表代表栈
stack1 = []
stack2 = []

# 插入节点
def append_tail(value):
    stack1.append(value)

# 删除节点
def delete_head():

    if len(stack2) <= 0:
        while len(stack1) > 0:
            data = stack1.pop()
            stack2.append(data)

    if len(stack2) == 0:
        print("队列为空")
        return

    head = stack2.pop()

    return head



append_tail(1)
append_tail(2)
append_tail(3)
append_tail(4)
print(stack1)

print(delete_head())
print(delete_head())

append_tail(5)
append_tail(6)

print(delete_head())
print(delete_head())
print(delete_head())
print(delete_head())
print(delete_head())
