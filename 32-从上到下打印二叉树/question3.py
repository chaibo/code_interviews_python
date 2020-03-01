"""
题目：之字形打印二叉树。
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此
类推。
"""


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree(root):
    if root is None:
        return

    # 行号从1开始
    # 奇数行栈
    stack1 = []
    # 偶数行栈
    stack2 = []

    # 当前行号
    current = 1

    stack1.append(root)

    while (not stack1) or (not stack2):
        node = None
        if current & 1 == 1:
            node = stack1.pop()
            if node.left:
                stack2.append(node.left)
            if node.right:
                stack2.append(node.right)
        else:
            node = stack2.pop()
            if node.right:
                stack1.append(node.right)
            if node.left:
                stack1.append(node.left)

        print(node.value, end=' ')

    if (not stack1) or (not stack2):
        print()
        current += 1
