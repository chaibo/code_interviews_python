"""
题目：不分行从上到下打印二叉树。
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
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

    while not print_queue.empty():
        node = print_queue.get(block=False)

        print(node.value, end=' ')

        if node.left:
            print_queue.put(node.left)
        if node.right:
            print_queue.put(node.right)
