"""
题目：平衡二叉树。
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左、右子树的
深度相差不超过 1，那么它就是一棵平衡二叉树。
"""


def is_balanced(root):
    if not root:
        return True, 0

    left, left_depth = is_balanced(root.left)
    right, right_depth = is_balanced(root.right)

    if left and right:
        diff = left_depth - right_depth
        if abs(diff) <= 1:
            depth = 1 + max(left_depth, right_depth)
            return True, depth

    return False, max(left_depth, right_depth)
