class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(n):
            row_sum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]
                prefix_sum = [0]
                cur_sum = 0
                for s in row_sum:
                    cur_sum += s
                    idx = bisect_left(prefix_sum, cur_sum - k)
                    if idx != len(prefix_sum):
                        res = max(res, cur_sum - prefix_sum[idx])
                    bisect.insort(prefix_sum, cur_sum)
        return res