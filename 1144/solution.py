class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        even_moves = odd_moves = 0
        for i in range(n):
            left = nums[i - 1] if i > 0 else float('inf')
            right = nums[i + 1] if i < n - 1 else float('inf')
            target = min(left, right) - 1
            if nums[i] >= target:
                if i % 2 == 0:
                    even_moves += nums[i] - target
                else:
                    odd_moves += nums[i] - target
        return min(even_moves, odd_moves)