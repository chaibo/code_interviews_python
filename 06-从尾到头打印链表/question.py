"""
题目：输入一个链表的头节点，从尾到头反过来打印出每个节点的值。
"""

class ListNode():
    """
    Python链表节点的定义。
    """
    def __init__(self, value):
        self.value = value
        self.next = None


# 解法一：栈
def solution1(head):

    stack = []
    node = head

    while node is not None:
        stack.append(node.value)
        node = node.next

    while len(stack) > 0:
        print(stack.pop(), end=' ')

    print()


# 解法二：递归
def solution2(head):
    if head is not None:
        solution2(head.next)
        print(head.value, end=' ')


l = [1, 2, 3, 4, 5]
head = pre = None

for i in l:
    node = ListNode(i)
    if head is None:
        head = node
        pre = node
    else:
        pre.next = node
        pre = node

solution1(head)
solution2(head)
print()
solution1(ListNode(4))
solution2(ListNode(5))

