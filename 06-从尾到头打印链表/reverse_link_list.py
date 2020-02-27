"""
反转链表
"""

class ListNode():
    """
    Python链表节点的定义。
    """
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_link_list(head):
    next = None
    pre = None

    while head is not None:
        next = head.next
        head.next = pre
        pre = head
        head = next

    return pre


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

node = head
while node is not None:
    print(node.value, end=' ')
    node = node.next
print()

head = reverse_link_list(head)
node = head
while node is not None:
    print(node.value, end=' ')
    node = node.next

