class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a