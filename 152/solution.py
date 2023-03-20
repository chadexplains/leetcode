class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = min_product = result = nums[0]
        for i in range(1, len(nums)):
            temp = max_product
            max_product = max(nums[i], max_product * nums[i], min_product * nums[i])
            min_product = min(nums[i], temp * nums[i], min_product * nums[i])
            result = max(result, max_product)
        return result