class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [envelope[1] for envelope in envelopes]
        return self.lengthOfLIS(heights)

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            i = bisect_left(dp, num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)