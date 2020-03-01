"""
题目：分行从上到下打印二叉树
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印一行。
"""

from queue import Queue


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_from_top_to_bottom(root):
    if root is None:
        return

    print_queue = Queue()
    print_queue.put(root)

    # 下一层节点数
    next_level = 0
    # 当前层还没有打印的节点数
    to_be_print = 1

    while not print_queue.empty():
        node = print_queue.get(block=False)

        print(node.value, end=' ')
        to_be_print -= 1

        if node.left:
            print_queue.put(node.left)
            next_level += 1
        if node.right:
            print_queue.put(node.right)
            next_level += 1

        if not to_be_print:
            print()
            to_be_print = next_level
            next_level = 0
