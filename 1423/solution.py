def maxScore(cardPoints, k):
    n = len(cardPoints)
    curr_sum = sum(cardPoints[:k])
    max_sum = curr_sum
    for i in range(k - 1, -1, -1):
        curr_sum -= cardPoints[i]
        curr_sum += cardPoints[n - (k - i)]
        max_sum = max(max_sum, curr_sum)
    return max_sum