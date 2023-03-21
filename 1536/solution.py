class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = [sum(row) for row in grid]
        swaps = 0
        for i in range(n):
            target_zeros = n - i - 1
            j = i
            while j < n and zeros[j] < target_zeros:
                j += 1
            if j == n:
                return -1
            while j > i:
                zeros[j], zeros[j-1] = zeros[j-1], zeros[j]
                swaps += 1
                j -= 1
        return swaps