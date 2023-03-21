class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == '(': stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                s = s[:j] + s[j:i+1][::-1].replace('(', '').replace(')', '') + s[i+1:]
        return s