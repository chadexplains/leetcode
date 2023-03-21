class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        # Perform DFS to find target node
        def dfs(node):
            if not node:
                return
            if node.val == k:
                target_node = node
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        # Perform BFS to find nearest leaf node
        queue = [(target_node, 0)]
        visited = set([target_node])
        while queue:
            node, dist = queue.pop(0)
            if not node.left and not node.right:
                return node.val
            if node.left and node.left not in visited:
                queue.append((node.left, dist + 1))
                visited.add(node.left)
            if node.right and node.right not in visited:
                queue.append((node.right, dist + 1))
                visited.add(node.right)