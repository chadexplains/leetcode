class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        count = 1
        for i in range(1, n+1):
            unique_digits = 9
            for j in range(9, 11-i, -1):
                unique_digits *= j
            count += unique_digits
        return count