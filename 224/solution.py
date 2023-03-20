class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        res = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                res += sign * num
                num = 0
                sign = 1
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == '(':  # push the result and sign onto the stack, start a new expression
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':  # evaluate the current expression and add to the previous result
                res += sign * num
                num = 0
                res *= stack.pop()  # sign
                res += stack.pop()  # result so far
        return res + sign * num