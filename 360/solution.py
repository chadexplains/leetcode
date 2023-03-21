class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        i = n - 1 if a >= 0 else 0
        while left <= right:
            left_val = a * nums[left] * nums[left] + b * nums[left] + c
            right_val = a * nums[right] * nums[right] + b * nums[right] + c
            if a >= 0:
                if left_val >= right_val:
                    result[i] = left_val
                    left += 1
                else:
                    result[i] = right_val
                    right -= 1
                i -= 1
            else:
                if left_val <= right_val:
                    result[i] = left_val
                    left += 1
                else:
                    result[i] = right_val
                    right -= 1
                i += 1
        return result