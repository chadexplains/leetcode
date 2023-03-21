class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = set()
        count = 0
        for num in nums:
            if num + k in seen:
                count += 1
            if num - k in seen:
                count += 1
            seen.add(num)
        return count