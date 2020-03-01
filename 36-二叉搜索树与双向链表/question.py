"""
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的节点，只能调整树中节点的指向。
"""


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def convert(root):
    last_node = convert_node(root)

    head = last_node
    while (head is not None) and (head.left is not  None):
        head = head.left

    return head


def convert_node(node):
    if node is None:
        return None

    last_node = None
    if node.left is not None:
        last_node = convert_node(node.left)

    node.left = last_node
    if last_node is not None:
        last_node.right = node

    last_node = node

    right_last_node = None
    if node.right is not None:
        right_last_node = convert_node(node.right)

    if right_last_node is not None:
        right_head = right_last_node
        while right_head.left is not None:
            right_head = right_head.left

        right_head.left = last_node
        last_node.right = right_head
        last_node = right_head

    return last_node
