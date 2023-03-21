```def longestConsecutive(root):
    def dfs(node, length):
        if not node:
            return 0
        if node.val == parent_val + 1:
            length += 1
        else:
            length = 1
        left_length = dfs(node.left, length)
        right_length = dfs(node.right, length)
        return max(length, left_length, right_length)
    return dfs(root, 1)```