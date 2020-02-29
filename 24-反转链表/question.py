"""
题目：反转链表。
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后的链表的头节点
"""

class ListNode():

    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_link_list1(head):
    next_node = None
    pre = None
    node = head

    while node is not None:
        next_node = node.next
        node.next = pre
        pre = node
        node = next_node

    return pre


# 递归实现
def reverse_link_list2(head):

    if (head is None) or (head.next is None):
        return head

    next_node = head.next

    new_head = reverse_link_list2(next_node)
    next_node.next = head
    head.next = None

    return new_head


def print_list(list):
    if list is None:
        print(None)
        return

    node = list
    while node:
        print(node.value, end=" ")
        node = node.next
    print()



node_a = ListNode("a")
node_b = ListNode("b")
node_c = ListNode("c")
node_d = ListNode("d")
node_e = ListNode("e")
node_f = ListNode("f")

test_list1 = node_a
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e
node_e.next = node_f

print_list(test_list1)
re_list1 = reverse_link_list1(test_list1)
print_list(re_list1)

test_list2 = None
re_list2 = reverse_link_list1(test_list2)
print_list(re_list2)

test_list3 = ListNode('1')
print_list(test_list3)
re_list3 = reverse_link_list1(test_list3)
print_list(re_list3)
