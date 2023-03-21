class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        m = len(queries)
        ans = [0] * m
        seg = [None] * (4 * n)
        def build(i, l, r):
            if l == r:
                seg[i] = (nums[l], nums[l])
            else:
                mid = (l + r) // 2
                build(2 * i + 1, l, mid)
                build(2 * i + 2, mid + 1, r)
                seg[i] = (min(seg[2 * i + 1][0], seg[2 * i + 2][0]), max(seg[2 * i + 1][1], seg[2 * i + 2][1]))
        def query(i, l, r, ql, qr):
            if ql <= l and r <= qr:
                return seg[i]
            elif qr < l or r < ql:
                return (float('inf'), float('-inf'))
            else:
                mid = (l + r) // 2
                left = query(2 * i + 1, l, mid, ql, qr)
                right = query(2 * i + 2, mid + 1, r, ql, qr)
                return (min(left[0], right[0]), max(left[1], right[1]))
        build(0, 0, n - 1)
        for i in range(m):
            l, r = queries[i]
            if l == r:
                ans[i] = -1
            else:
                mn, mx = query(0, 0, n - 1, l, r - 1)
                ans[i] = mx - mn
        return ans