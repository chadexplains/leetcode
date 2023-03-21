class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        result = ""
        for c in S:
            if c == "(" and len(stack) > 0:
                result += c
            elif c == ")" and len(stack) > 1:
                result += c
            if c == "(":
                stack.append(c)
            else:
                stack.pop()
        return result