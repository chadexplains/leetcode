def cheapestJump(A: List[int], B: int) -> List[int]:
    n = len(A)
    dp = [float('inf')] * n
    dp[0] = 0
    path = [-1] * n
    for i in range(n):
        if A[i] == -1:
            continue
        for j in range(i+1, min(i+B+1, n)):
            if A[j] == -1:
                continue
            if dp[j] > dp[i] + A[j]:
                dp[j] = dp[i] + A[j]
                path[j] = i
    if dp[-1] == float('inf'):
        return []
    res = []
    cur = n-1
    while cur != -1:
        res.append(cur+1)
        cur = path[cur]
    return res[::-1]