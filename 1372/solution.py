class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestZigZag(root: TreeNode) -> int:
    queue = [(root, True)]
    longest_path = 0
    while queue:
        node, is_right = queue.pop(0)
        if node:
            longest_path = max(longest_path, node.val)
            if is_right:
                queue.append((node.left, False))
                queue.append((node.right, True))
            else:
                queue.append((node.right, True))
                queue.append((node.left, False))
    return longest_path