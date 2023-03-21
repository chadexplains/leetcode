class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        max_len = 0
        cum_sum = 0
        sum_index = {}
        for i, hour in enumerate(hours):
            cum_sum += 1 if hour > 8 else -1
            if cum_sum > 0:
                max_len = i + 1
            else:
                if cum_sum - 1 in sum_index:
                    max_len = max(max_len, i - sum_index[cum_sum - 1])
                if cum_sum not in sum_index:
                    sum_index[cum_sum] = i
        return max_len