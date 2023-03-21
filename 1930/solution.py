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
            mn, mx = tree[1]
            if l > 0:
                lmn, lmx = tree_query(1, 0, n - 1, 0, l - 1)
                mn, mx = min(mn, lmn), max(mx, lmx)
            if r < n - 1:
                rmn, rmx = tree_query(1, 0, n - 1, r + 1, n - 1)
                mn, mx = min(mn, rmn), max(mx, rmx)
            ans.append(mx - mn)
        return ans

    def tree_query(node, start, end, l, r):
        if r < start or end < l:
            return [float('inf'), float('-inf')]
        if l <= start and end <= r:
            return tree[node]
        mid = (start + end) // 2
        lmn, lmx = tree_query(node * 2, start, mid, l, r)
        rmn, rmx = tree_query(node * 2 + 1, mid + 1, end, l, r)
        return [min(lmn, rmn), max(lmx, rmx)]