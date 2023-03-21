class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            count, start = 0, 0
            for i in range(n):
                while nums[i] - nums[start] > mid:
                    start += 1
                count += i - start
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left