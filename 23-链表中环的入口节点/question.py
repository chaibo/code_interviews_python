"""
题目：如果一个链表包含环，如何找出环的入口节点？
"""

class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


def metting_node(list):
    """
    在链表中存在环的情况下，找到位于环中的一个节点。
    :param list: 链表头节点
    :return: 环中的节点或None
    """

    if list is None:
        return None

    slow = list.next
    if slow is None:
        return None

    fast = slow.next

    while (fast is not None) and (slow is not None):
        if fast == slow:
            return fast

        slow = slow.next

        fast = fast.next
        if fast is not None:
            fast = fast.next

    return None


def entry_node_of_loop(list):
    """
    在链表中存在环的情况下，找到环的入口点。
    :param list: 链表头节点
    :return: 环的入口点或None
    """

    met_node = metting_node(list)
    if met_node is None:
        return None

    # 得到环中节点的数量
    nodes_in_loop = 1
    node = met_node
    while node.next != met_node:
        node = node.next
        nodes_in_loop += 1

    node1 = list
    for i in range(nodes_in_loop):
        node1 = node1.next

    node2 = list
    while node1 != node2:
        node1 = node1.next
        node2 = node2.next

    return node1



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

print(entry_node_of_loop(test_list1))

node_f.next = node_c

print(entry_node_of_loop(test_list1).value)

print(entry_node_of_loop(None))

test_list2 = ListNode('1')
test_list2.next = test_list2

print(entry_node_of_loop(test_list2).value)
