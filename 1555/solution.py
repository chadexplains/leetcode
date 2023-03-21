def minDays(n: int) -> int:
    memo = {}
    def dp(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in memo:
            return memo[n]
        if n % 2 == 0:
            memo[n] = 1 + dp(n // 2)
        else:
            memo[n] = 1 + dp(n - 1)
        return memo[n]
    return dp(n)