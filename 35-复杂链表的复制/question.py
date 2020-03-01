"""
题目：请实现函数 clone(head)，复制一个复杂链表。
在复杂链表中，每个节点除了有一个 next 指向下一个节点，
还有一个 sibling 指向链表中的任意节点或者 None。
"""


class ComplexListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.sibling = None


def clone(head):
    clone_nodes(head)
    connect_sibling_nodes(head)
    return reconnect_nodes(head)


def clone_nodes(head):
    """
    根据原始链表的每个节点 N，创建节点 N'，并把 N' 链接到 N 的后面。
    """
    node = head
    while node:
        clone_node = ComplexListNode(node.value)
        clone_node.next = node.next
        clone_node.sibling = None
        node.next = clone_node
        node = clone_node.next


def connect_sibling_nodes(head):
    node = head
    while node:
        clone_node = node.next
        if node.sibling:
            clone_node.sibling = node.sibling.next

        node = clone_node.next


def reconnect_nodes(head):
    node = head
    clone_head = None
    clone_node = None

    if node:
        clone_head = node.next
        clone_node = node.next
        node.next = clone_node.next

    while node:
        clone_node.next = node.next
        clone_node = node.next
        node.next = clone_node.next
        node = node.next

    return clone_head

