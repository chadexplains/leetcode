class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        res = [0] * n
        left, right = float('-inf'), float('inf')
        for i in range(n):
            if S[i] == C:
                left = i
            res[i] = i - left
        for i in range(n - 1, -1, -1):
            if S[i] == C:
                right = i
            res[i] = min(res[i], right - i)
        return res