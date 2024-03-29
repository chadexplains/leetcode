def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        for i, a in enumerate(A):
            if not stack or A[stack[-1]] > a:
                stack.append(i)
        res = 0
        for j in range(len(A) - 1, -1, -1):
            while stack and A[stack[-1]] <= A[j]:
                res = max(res, j - stack.pop())
        return res