class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        res = [[0] * c for _ in range(r)]
        for i in range(r * c):
            res[i // c][i % c] = nums[i // n][i % n]
        return res