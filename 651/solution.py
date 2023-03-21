def maxA(N):
    factors = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            factors.append(i)
            if i != N // i:
                factors.append(N // i)
    dp = [0] * (N+1)
    for f in factors:
        for j in range(f, N+1):
            dp[j] = max(dp[j], dp[j-f]*(j-f+1))
    return dp[N]