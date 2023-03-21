class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def height(node):
            if not node:
                return -1
            h = 1 + max(height(node.left), height(node.right))
            if h == len(result):
                result.append([])
            result[h].append(node.val)
            return h
        result = []
        height(root)
        return result[::-1]