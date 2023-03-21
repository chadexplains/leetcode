class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
        if factors[-1] ** 2 == n:
            factors.pop()
        for i in range(len(factors) - 1, -1, -1):
            if factors[i] ** 2 != n:
                factors.append(n // factors[i])
        return -1 if k > len(factors) else factors[k - 1]