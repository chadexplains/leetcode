class Solution:
    def smallestSubsequence(self, s: str, k: int, target: str) -> str:
        stack = []
        target_count = k - 1
        for i, c in enumerate(s):
            while stack and stack[-1] > c and len(s) - i > target_count:
                if stack[-1] == target:
                    target_count += 1
                stack.pop()
            if c == target or len(stack) < k:
                stack.append(c)
                if c == target:
                    target_count -= 1
            if target_count == 0:
                break
        return ''.join(stack)