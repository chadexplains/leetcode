class Solution:
    def expand(self, S: str) -> List[str]:
        stack = [[]]
        for c in S:
            if c == '{':
                stack.append([])
            elif c == '}':
                last = stack.pop()
                stack[-1] = [s + l for s in stack[-1] for l in last]
            else:
                stack[-1].append(c)
        return sorted(stack[-1])