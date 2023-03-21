class Solution:
    def secondHighest(self, s: str) -> int:
        largest = second_largest = -1
        for c in s:
            if c.isdigit():
                digit = int(c)
                if digit > largest:
                    second_largest = largest
                    largest = digit
                elif digit != largest and digit > second_largest:
                    second_largest = digit
        return second_largest