def minOperations(boxes):
    n = len(boxes)
    left = [0] * n
    right = [0] * n
    res = [0] * n
    for i in range(1, n):
        left[i] = left[i-1] + int(boxes[i-1])
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] + int(boxes[i+1])
    for i in range(n):
        res[i] = left[i] + right[i]
    return res