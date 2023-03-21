class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        pairs = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] == k:
                    pairs.add((nums[i], nums[j]))
        return len(pairs)