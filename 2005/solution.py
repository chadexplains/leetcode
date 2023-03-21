class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        m = len(queries)
        tree = [None] * (4 * n)
        def build(node, start, end):
            if start == end:
                tree[node] = [nums[start], nums[start]]
            else:
                mid = (start + end) // 2
                build(node * 2, start, mid)
                build(node * 2 + 1, mid + 1, end)
                tree[node] = [min(tree[node * 2][0], tree[node * 2 + 1][0]), max(tree[node * 2][1], tree[node * 2 + 1][1])]
        build(1, 0, n - 1)
        ans = []
        for i in range(m):
            l, r = queries[i]
            mn, mx = float('inf'), float('-inf')
            def query(node, start, end):
                nonlocal mn, mx
                if start > r or end < l:
                    return
                if l <= start and end <= r:
                    mn = min(mn, tree[node][0])
                    mx = max(mx, tree[node][1])
                else:
                    mid = (start + end) // 2
                    query(node * 2, start, mid)
                    query(node * 2 + 1, mid + 1, end)
            query(1, 0, n - 1)
            if mn == float('inf'):
                ans.append(-1)
            else:
                ans.append(mx - mn)
        return ans
