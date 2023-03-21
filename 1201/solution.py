class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)
        def lcm(x, y):
            return x * y // gcd(x, y)
        ab, ac, bc = lcm(a, b), lcm(a, c), lcm(b, c)
        abc = lcm(ab, c)
        left, right = 1, 2 * 10 ** 9
        while left < right:
            mid = (left + right) // 2
            count = mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc
            if count < n:
                left = mid + 1
            else:
                right = mid
        return left