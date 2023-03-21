class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total_sum = sum(nums)
        sub_sum = 0
        subsequence = []
        for num in nums:
            sub_sum += num
            subsequence.append(num)
            if sub_sum > total_sum - sub_sum:
                break
        return subsequence