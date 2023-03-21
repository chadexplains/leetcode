class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        cloned = {}
        def dfs(node):
            if not node:
                return None
            cloned_node = Node(node.val, [])
            cloned[node] = cloned_node
            for child in node.children:
                cloned_node.children.append(dfs(child))
            return cloned_node
        return dfs(root)