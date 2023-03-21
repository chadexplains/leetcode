def pourWater(heights, V, K):
    n = len(heights)
    for i in range(V):
        j = K
        while j > 0 and heights[j] >= heights[j - 1]:
            j -= 1
        while j < n - 1 and heights[j] >= heights[j + 1]:
            j += 1
        while j > K and heights[j] >= heights[j - 1]:
            j -= 1
        if j != K:
            heights[j] += 1
    return heights