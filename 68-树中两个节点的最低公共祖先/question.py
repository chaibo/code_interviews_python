"""
题目：求一棵普通树中，两个节点的最低公共祖先。
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def get_last_comm_parent(root, node1, node2):
    if (not root) or (not node1) or (not node2):
        return None

    path1 = []
    path2 = []
    get_node_path(root, node1, path1)
    get_node_path(root, node2, path2)

    return get_last_comm_node(path1, path2)


def get_node_path(root, node, path):
    if root == node:
        return True

    path.append(root)
    found = False

    children = root.children

    for child in children:
        found = get_node_path(child, node, path)

        if found:
            break

    if not found:
        path.pop()

    return found


def get_last_comm_node(path1, path2):
    length1 = len(path1)
    length2 = len(path2)

    index1 = index2 = 0

    last = None

    while (index1 < length1) and (index2 < length2):
        if path1[index1] != path2[index2]:
            break
        else:
            last = path1[index1]
            index1 += 1
            index2 += 1

    return last
