class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        n = 2 * N
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                j = n // i
                if (j - i + 1) % 2 == 0 and (j - i + 1) > 0:
                    count += 1
        return count