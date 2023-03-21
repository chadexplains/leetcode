class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        count = 0
        for c in S:
            if c == '(': stack.append(c)
            elif stack: stack.pop()
            else: count += 1
        return count + len(stack)