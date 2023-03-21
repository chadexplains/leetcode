class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        prev = self.kthGrammar(N-1, (K+1)//2)
        if prev == 0:
            return 0 if K % 2 == 1 else 1
        else:
            return 1 if K % 2 == 1 else 0