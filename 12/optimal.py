class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        fives = ['', 'V', 'X', 'L', 'C', 'D', 'M']
        roman_numeral = ''
        i = 0
        while num > 0:
            digit = num % 10
            if digit == 4:
                roman_numeral = ones[i] + fives[i] + roman_numeral
            elif digit == 9:
                roman_numeral = ones[i] + fives[i + 1] + roman_numeral
            else:
                roman_numeral = ones[digit] + fives[i] * (digit // 5) + ones[digit % 5] + roman_numeral
            num //= 10
            i += 2
        return roman_numeral
