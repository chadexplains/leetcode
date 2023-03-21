class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        num_primes = sum(primes)
        num_non_primes = n - num_primes
        return (math.factorial(num_primes) * math.factorial(num_non_primes)) % (10 ** 9 + 7)