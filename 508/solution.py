class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            freq[s] += 1
            return s
        freq = collections.Counter()
        dfs(root)
        max_freq = max(freq.values() or [0])
        return [s for s in freq.keys() if freq[s] == max_freq]