class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        prev_value = 0
        for c in s:
            value = roman_numerals[c]
            if value > prev_value:
                integer += value - 2 * prev_value
            else:
                integer += value
            prev_value = value
        return integer
