class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        set_sum = sum(set(nums))
        return [actual_sum - set_sum, expected_sum - set_sum]