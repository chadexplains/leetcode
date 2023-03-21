class Solution:
    def sumGame(self, nums: str) -> bool:
        n = len(nums)
        left_sum = right_sum = left_q = right_q = 0
        for i in range(n):
            if i < n // 2:
                if nums[i] == '?':
                    left_q += 1
                else:
                    left_sum += int(nums[i])
            else:
                if nums[i] == '?':
                    right_q += 1
                else:
                    right_sum += int(nums[i])
        if left_q == right_q:
            return left_sum != right_sum
        if left_q > right_q:
            left_q, right_q = right_q, left_q
            left_sum, right_sum = right_sum, left_sum
        diff_q = right_q - left_q
        diff_sum = right_sum - left_sum
        if diff_sum >= 0:
            return True
        if diff_q % 2 == 0:
            return False
        return abs(diff_sum) > (diff_q // 2) * 9