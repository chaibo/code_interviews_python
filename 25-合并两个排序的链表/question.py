"""
题目：输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
例如，链表 1 -> 3 -> 5 -> 7 和链表 2 -> 4 -> 6 -> 8 合并之后的升序链表
为 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8。
"""

class ListNode():

    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(list):
    if list is None:
        print(None)
        return

    node = list
    while node:
        print(node.value, end=" ")
        node = node.next
    print()


def merge_list(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    merged_head = None

    if head1.value < head2.value:
        merged_head = head1
        merged_head.next = merge_list(head1.next, head2)
    else:
        merged_head = head2
        merged_head.next = merge_list(head1, head2.next)

    return merged_head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)

list1 = node1
node1.next = node3
node3.next = node5
node5.next = node7

list2 = node2
node2.next = node4
node4.next = node6
node6.next = node8

print_list(list1)
print_list(list2)
merge_list1 = merge_list(list1, list2)
print_list(merge_list1)

print_list(merge_list(None, None))
print_list(merge_list(list1, None))
print_list(merge_list(None, list1))
