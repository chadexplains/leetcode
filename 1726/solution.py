class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = {}
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                if product in products:
                    products[product] += 1
                else:
                    products[product] = 1
        for freq in products.values():
            if freq > 1:
                count += freq * (freq-1) // 2
        return count