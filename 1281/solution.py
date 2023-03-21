class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = str(n)
        product = 1
        sum = 0
        for digit in digits:
            product *= int(digit)
            sum += int(digit)
        return product - sum