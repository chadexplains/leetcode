class Solution:
    def getMedian(self, nums: List[int], freq: List[int]) -> float:
        n = len(nums)
        arr = [(nums[i], freq[i]) for i in range(n)]
        arr.sort()
        total_freq = sum(freq)
        if total_freq % 2 == 1:
            mid_freq = total_freq // 2 + 1
            cum_freq = 0
            for i in range(n):
                cum_freq += arr[i][1]
                if cum_freq >= mid_freq:
                    return arr[i][0]
        else:
            mid_freq1 = total_freq // 2
            mid_freq2 = total_freq // 2 + 1
            cum_freq = 0
            mid_nums = []
            for i in range(n):
                cum_freq += arr[i][1]
                if cum_freq >= mid_freq1 and not mid_nums:
                    mid_nums.append(arr[i][0])
                if cum_freq >= mid_freq2:
                    mid_nums.append(arr[i][0])
                    break
            return sum(mid_nums) / 2.0