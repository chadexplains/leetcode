class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        deque = collections.deque([root])
        flag = True
        while deque:
            level = []
            for _ in range(len(deque)):
                node = deque.popleft()
                level.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            if flag:
                result.append(level)
            else:
                result.append(level[::-1])
            flag = not flag
        return result