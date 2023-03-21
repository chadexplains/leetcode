def canReach(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    dp = [False] * n
    dp[0] = True
    for i in range(n):
        if not dp[i]:
            continue
        for j in range(i + minJump, min(i + maxJump + 1, n)):
            if s[j] == '0':
                dp[j] = True
                if j == n - 1:
                    return True
    return dp[n - 1]
