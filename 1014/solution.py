def maxScoreSightseeingPair(self, A: List[int]) -> int:
    max_score = 0
    max_ai_plus_i = 0
    for j in range(len(A)):
        score = A[j]-j+max_ai_plus_i
        max_score = max(max_score, score)
        max_ai_plus_i = max(max_ai_plus_i, A[j]+j)
    return max_score