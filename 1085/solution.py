class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        min_num = min(A)
        sum_digits = 0
        while min_num > 0:
            sum_digits += min_num % 10
            min_num //= 10
        return 1 if sum_digits % 2 == 1 else 0