class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        def convert(s):
            if '(' not in s:
                return Fraction(s)
            non_repeat = s.split('(')[0]
            repeat = s.split('(', 1)[1][:-1]
            repeat_non_zero = repeat.lstrip('0')
            if len(repeat_non_zero) == 0:
                repeat_non_zero = '0'
            repeat_denominator = (10 ** len(repeat)) - 1
            non_repeat_contrib = Fraction(non_repeat)
            repeat_contrib = Fraction(repeat_non_zero, repeat_denominator)
            return non_repeat_contrib + repeat_contrib
        return convert(S) == convert(T)