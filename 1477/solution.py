class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left, right = [float('inf')] * n, [float('inf')] * n
        d = {0: -1}
        s = 0
        l = float('inf')
        for i in range(n):
            s += arr[i]
            if s - target in d:
                l = min(l, i - d[s - target])
            left[i] = l
            d[s] = i
        d = {0: n}
        s = 0
        l = float('inf')
        for i in range(n - 1, -1, -1):
            s += arr[i]
            if s - target in d:
                l = min(l, d[s - target] - i)
            right[i] = l
            d[s] = i
        res = float('inf')
        for i in range(n - 1):
            res = min(res, left[i] + right[i + 1])
        return res if res != float('inf') else -1