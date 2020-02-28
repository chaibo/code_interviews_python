"""
题目：在 O(1) 时间内删除链表节点。
给定单链表的头节点和一个节点，定义一个函数在 O(1) 时间内删除该节点。
"""

class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node(list, delete_node):

    if (list is None) or (delete_node is None):
        return list

    # 要删除的节点不是尾节点
    if delete_node.next is not None:
        next = delete_node.next
        delete_node.value = next.value
        delete_node.next = next.next
        next.next = None
    # 链表只有一个节点，删除该节点
    elif list == delete_node:
        del delete_node
        list = None
    # 链表中有多个节点，删除尾节点
    else:
        node = list
        while node.next != delete_node:
            node = node.next

        node.next = None

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


node_a = ListNode("a")
node_b = ListNode("b")
node_c = ListNode("c")
node_d = ListNode("d")
node_e = ListNode("e")
node_f = ListNode("f")

test_list1 = None
result_list1 = delete_node(test_list1, None)
print_list(result_list1)

test_list2 = node_a
result_list2 = delete_node(test_list2, None)
print_list(result_list2)

test_list3 = node_a
result_list3 = delete_node(test_list3, node_a)
print_list(result_list3)

test_list4 = node_a
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e
node_e.next = node_f
print_list(test_list4)

result_list4 = delete_node(test_list4, node_a)
print_list(result_list4)

result_list5 = delete_node(test_list4, node_d)
print_list(result_list5)


result_list6 = delete_node(test_list4, node_f)
print_list(result_list6)
