class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def inorder(node):
            nonlocal curr_val, curr_count, max_count, modes
            if not node:
                return
            inorder(node.left)
            if node.val == curr_val:
                curr_count += 1
            else:
                curr_val = node.val
                curr_count = 1
            if curr_count > max_count:
                max_count = curr_count
                modes = [curr_val]
            elif curr_count == max_count:
                modes.append(curr_val)
            inorder(node.right)
        curr_val = None
        curr_count = 0
        max_count = 0
        modes = []
        inorder(root)
        return modes