"""
题目：删除链表中重复的节点。
在一个排序的链表中，如何删除重复的节点？
例如，链表 1->2->3->3->4->4->5 中重复的节点被删除之后，链表变为 1->2>5。
"""

class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, value):
        node = self
        while node.next:
            node = node.next
        node.next = ListNode(value)


def delete_duplication(list):
    pre_node = None
    node = list
    while node is not None:
        next_node = node.next

        if (next_node is not None) and (next_node.value == node.value):
            value = node.value
            while (next_node is not None) and (next_node.value == value):
                next_node = next_node.next

            if pre_node is None:
                list = next_node
            else:
                pre_node.next = next_node
            node = next_node
        else:
            pre_node = node
            node = next_node

    return list


def print_list(list):
    if list is None:
        print(None)
        return

    node = list
    while node:
        print(node.value, end=" ")
        node = node.next
    print()


test_list1 = None
print_list(delete_duplication(test_list1))

test_list2 = ListNode(1)
print_list(delete_duplication(test_list2))

test_list3 = ListNode(1)
test_list3.append(1)
test_list3.append(1)
test_list3.append(1)
test_list3.append(1)
print_list(delete_duplication(test_list3))

test_list4 = ListNode(1)
test_list4.append(1)
test_list4.append(1)
test_list4.append(2)
test_list4.append(3)
test_list4.append(3)
test_list4.append(4)
test_list4.append(5)
test_list4.append(5)
print_list(delete_duplication(test_list4))
