class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        table = defaultdict(list)
        while queue:
            node, pos = queue.popleft()
            table[pos].append(node.val)
            if node.left:
                queue.append((node.left, pos - 1))
            if node.right:
                queue.append((node.right, pos + 1))
        return [table[i] for i in sorted(table)]