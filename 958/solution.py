class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = [root]
        null_node_found = False
        while queue:
            node = queue.pop(0)
            if node is None:
                null_node_found = True
            else:
                if null_node_found:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True