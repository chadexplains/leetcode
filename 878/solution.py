class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        lcm = A * B // gcd(A, B)
        left, right = min(A, B), N * min(A, B)
        while left < right:
            mid = (left + right) // 2
            if mid // A + mid // B - mid // lcm < N:
                left = mid + 1
            else:
                right = mid
        return left % (10**9 + 7)