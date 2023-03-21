class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        res = nums[0]
        for num in nums:
            res = gcd(res, num)
            if res == 1:
                return True
        return False