"""
题目：输入两个链表，找出它们的第一个公共节点。
"""


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def find_first_common_node(head1, head2):
    len1 = get_list_len(head1)
    len2 = get_list_len(head2)

    len_dif = len1 - len2

    head_long = head1
    head_short = head2

    if len1 < len2:
        head_long = head2
        head_short = head1
        len_dif = len2 - len1

    for i in range(len_dif):
        head_long = head_long.next

    while head_long and head_short and (head_long != head_short):
        head_long = head_long.next
        head_short = head_short.next

    return head_long


def get_list_len(head):
    node = head
    length = 0

    while node:
        length += 1
        node = node.next

    return length
