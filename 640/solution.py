class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        left_coef, left_const = self.parse(left)
        right_coef, right_const = self.parse(right)
        coef = left_coef - right_coef
        const = right_const - left_const
        if coef == 0 and const == 0:
            return 'Infinite solutions'
        elif coef == 0:
            return 'No solution'
        else:
            return 'x=' + str(const // coef)

    def parse(self, expr: str) -> Tuple[int, int]:
        coef = const = num = 0
        sign = 1
        for c in expr:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == 'x':
                coef += num * sign or sign
                num = 0
            else:
                const += num * sign
                num = 0
                if c == '-':
                    sign = -1
        const += num * sign
        return coef, const