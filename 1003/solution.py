class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c != 'c':
                stack.append(c)
            else:
                if len(stack) < 2 or stack[-2:] != ['a', 'b']:
                    return False
                stack.pop()
                stack.pop()
        return len(stack) == 0