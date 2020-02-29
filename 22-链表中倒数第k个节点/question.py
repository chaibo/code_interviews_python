"""
题目：输入一个链表，输出该链表中倒数第 k 个节点。
为了符合大多数人的习惯，本题从 1 开始计数，即链表的尾节点是倒数第 1 个节点。
例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。
这个链表的倒数第 3 个节点是值为 4 的节点。
"""

class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


def find_kth(list, k):
    if (list is None) or (k <= 0):
        return None

    ahead = list

    for i in range(k-1):
        if ahead.next is None:
            return None

        ahead = ahead.next

    behind = list

    while ahead.next is not None:
        ahead = ahead.next
        behind = behind.next

    return behind

node_a = ListNode("a")
node_b = ListNode("b")
node_c = ListNode("c")
node_d = ListNode("d")
node_e = ListNode("e")
node_f = ListNode("f")

test_list = node_a
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e
node_e.next = node_f

print(find_kth(None, 4))
print(find_kth(test_list, 0))
print(find_kth(test_list, 3).value)
print(find_kth(test_list, 1).value)
print(find_kth(test_list, 6).value)
print(find_kth(test_list, 9))
