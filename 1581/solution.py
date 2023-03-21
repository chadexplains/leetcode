class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        if fib[-1] == k:
            return 1
        def helper(n):
            if n == 0:
                return 0
            i = bisect.bisect_right(fib, n)
            return helper(n - fib[i-1]) + 1
        return helper(k)