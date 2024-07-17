class TreeNode(object):
    def __init__(self, root=None, val=0, left=None, right=None):
        self.root = root
        self.val = val
        self.left = left
        self.right = right

    def update(self, root=None, val=None, left=None, right=None):
        if root is not None:
            self.root = root
        if val is not None:
            self.val = val
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right


class Solution(object):
    result = []

    def findRoot(self, tree, current_val):
        current_node = tree[current_val]
        if current_node.root == current_val:
            return current_node

        return self.findRoot(tree, current_node.root)

    def createBinaryTree(self, descriptions):
        tree = {}
        any_node = -1

        for node in descriptions:
            parent = node[0]
            child = node[1]
            any_node = parent
            if parent in tree:
                parent_node = tree[parent]
            else:
                parent_node = TreeNode(parent, parent, None, None)
                tree[parent] = parent_node

            if child not in tree:
                tree[child] = TreeNode(parent_node.root, child, None, None)
            else:
                tree[child].update(parent_node.root, None, None, None)

            if node[2] == 1:
                tree[parent].left = tree[child]
            else:
                tree[parent].right = tree[child]

        return self.findRoot(tree, any_node)