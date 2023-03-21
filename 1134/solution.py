class Solution:
    def isArmstrong(self, n: int) -> bool:
        num_str = str(n)
        num_digits = len(num_str)
        armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
        return armstrong_sum == n