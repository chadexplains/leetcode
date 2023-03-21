class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = collections.Counter(nums)
        nums.sort(reverse=True)
        return sum((count[nums[i]] * (n-i-1)) for i in range(n-1))
