"""
题目：输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中
序遍历的结果中都不含重复数字。例如，输入前序遍历序列{1, 2, 4, 7, 3, 5, 6, 8}和
中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}，重建二叉树并输出它的头节点。
"""

class BinaryTreeNode():
    """
    Python二叉树节点的定义。
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def construct(pre_order, in_order):

    if (pre_order is None) or (in_order is None) \
            or (len(pre_order) <= 0) or (len(in_order) <= 0) \
            or (len(pre_order) != len(in_order)):
        raise Exception("Invalid input!")

    root_value = pre_order[0]
    root = BinaryTreeNode(root_value)

    if len(pre_order) == 1:
        if (len(in_order) == 1) and (in_order[0] == pre_order[0]):
            return root
        else:
            raise Exception("Invalid input!")

    root_inorder = 0
    while (root_inorder < len(in_order)) \
            and (in_order[root_inorder] != root_value):
        root_inorder += 1

    if root_inorder >= len(in_order):
        raise Exception("Invalid input!")

    left_len = root_inorder
    if left_len > 0:
        # 构建左子树
        root.left = \
            construct(pre_order[1:root_inorder + 1], in_order[:root_inorder])
    if root_inorder < (len(in_order) - 1):
        # 构建右子树
        root.right = \
            construct(pre_order[root_inorder + 1 :], in_order[root_inorder + 1 :])

    return root


pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
in_order = [4, 7, 2, 1, 5, 3, 8, 6]

root = construct(pre_order, in_order)

def pre_order(root):
    if root is not None:
        print(root.value, end=' ')
        pre_order(root.left)
        pre_order(root.right)


def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.value, end=' ')
        in_order(root.right)

pre_order(root)
print()
in_order(root)




