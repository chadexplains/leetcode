class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def traverse(node):
            if not node:
                return 'null'
            left = traverse(node.left)
            right = traverse(node.right)
            subtree = left + ',' + right + ',' + str(node.val)
            if subtree in subtrees:
                if subtrees[subtree] == 1:
                    result.append(node)
                subtrees[subtree] += 1
            else:
                subtrees[subtree] = 1
            return subtree
        result = []
        subtrees = {}
        traverse(root)
        return result