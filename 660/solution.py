class Solution:
    def newInteger(self, n: int) -> int:
        ans = 0
        base = 1
        while n:
            ans += n % 9 * base
            n //= 9
            base *= 10
        return ans