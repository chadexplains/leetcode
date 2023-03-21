class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        first_neg, first_zero, max_len, curr_len, neg_count = -1, 0, 0, 0, 0
        for i, num in enumerate(nums):
            if num == 0:
                curr_len, neg_count, first_neg = 0, 0, -1
                first_zero = i + 1
            else:
                curr_len += 1
                if num < 0:
                    neg_count += 1
                    if first_neg == -1:
                        first_neg = i
                if neg_count % 2 == 0:
                    max_len = max(max_len, curr_len)
                else:
                    max_len = max(max_len, i - first_neg)
        return max_len