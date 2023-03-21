class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        sorted_nums = sorted(nums, reverse=True)
        smallest = sorted_nums[-1]
        res = 0
        for i, num in enumerate(sorted_nums):
            if num == smallest:
                break
            res += freq[num] * (num - smallest)
            smallest = num
        return res