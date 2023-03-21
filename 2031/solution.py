class Solution:
    def smallestSubsequence(self, s: str, k: int, target: str) -> str:
        stack = []
        target_set = set(target)
        target_count = k - target.count(target[0])
        for i, c in enumerate(s):
            while stack and stack[-1] > c and len(s) - i + len(stack) > k and (stack[-1] != target or target_count > 0):
                if stack[-1] == target:
                    target_count += 1
                stack.pop()
            if c in target_set:
                target_count -= 1
            stack.append(c)
            if len(stack) == k:
                return ''.join(stack)
        return ''