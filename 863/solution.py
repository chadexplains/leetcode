class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root, None)
        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            node, dist = queue.popleft()
            for nei in (node.left, node.right, node.parent):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist+1))
        return []