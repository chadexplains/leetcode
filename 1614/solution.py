class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(': 
                stack.append(c)
                depth += 1
                max_depth = max(max_depth, depth)
            elif c == ')':
                stack.pop()
                depth -= 1
        return max_depth