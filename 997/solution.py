def findJudge(N: int, trust: List[List[int]]) -> int:
    trust_counts = [0] * (N+1)
    for a, b in trust:
        trust_counts[a] -= 1
        trust_counts[b] += 1
    for i in range(1, N+1):
        if trust_counts[i] == N-1:
            return i
    return -1