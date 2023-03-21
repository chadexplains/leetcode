class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(node, i):
            if not node or i == len(arr) or node.val != arr[i]:
                return False
            if not node.left and not node.right and i == len(arr) - 1:
                return True
            return dfs(node.left, i+1) or dfs(node.right, i+1)
        return dfs(root, 0)