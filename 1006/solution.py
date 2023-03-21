class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1
        elif N == 2:
            return 2
        elif N == 3:
            return 6
        elif N == 4:
            return 7
        else:
            return N * (N - 1) // (N - 2) + (N - 3) - self.clumsy(N - 4)