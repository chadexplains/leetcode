class Solution:
    def countOrders(self, n: int) -> int:
        return math.factorial(n*(n+1)//2) % (10**9 + 7)