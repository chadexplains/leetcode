class Solution:
    def confusingNumberII(self, n: int) -> int:
        confusing_digits = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        def is_confusing(num):
            rotated = 0
            original = num
            while num:
                digit = num % 10
                if digit not in confusing_digits:
                    return False
                rotated = rotated * 10 + confusing_digits[digit]
                num //= 10
            return rotated != original
        def backtrack(num):
            count = is_confusing(num)
            for digit, rotated in confusing_digits.items():
                if num * 10 + digit <= n:
                    count += backtrack(num * 10 + digit)
            return count
        return backtrack(0)