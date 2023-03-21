class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def dfs(node, parent):
            if node:
                parent[node.val] = parent.get(node.val, None)
                if node.left:
                    parent[node.left.val] = node
                    dfs(node.left, parent)
                if node.right:
                    parent[node.right.val] = node
                    dfs(node.right, parent)
        parent = {}
        dfs(root, parent)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p.val]
        while q not in ancestors:
            q = parent[q.val]
        lca = q
        distance = 0
        stack = [(lca, 0)]
        while stack:
            node, dist = stack.pop()
            if node.val == p:
                return distance + dist
            if node.left and node.left.val != lca.val:
                stack.append((node.left, dist + 1))
            if node.right and node.right.val != lca.val:
                stack.append((node.right, dist + 1))
            if node.val != lca.val:
                distance += 1
        return distance