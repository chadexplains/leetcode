class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        super_ugly = [1]
        indices = [0] * len(primes)
        for i in range(n):
            next_super_ugly = float('inf')
            next_possible = []
            for j in range(len(primes)):
                possible = primes[j] * super_ugly[indices[j]]
                if possible < next_super_ugly:
                    next_possible = [possible]
                    next_super_ugly = possible
                elif possible == next_super_ugly:
                    next_possible.append(possible)
                
            for j in range(len(primes)):
                if primes[j] * super_ugly[indices[j]] == next_super_ugly:
                    indices[j] += 1
            super_ugly.append(next_super_ugly)
        return super_ugly[-1]