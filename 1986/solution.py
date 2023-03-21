def minOperations(boxes):
    n = len(boxes)
    prefix_sum = [0]*n
    suffix_sum = [0]*n
    for i in range(1,n):
        prefix_sum[i] = prefix_sum[i-1] + int(boxes[i-1])
    for i in range(n-2,-1,-1):
        suffix_sum[i] = suffix_sum[i+1] + int(boxes[i+1])
    return [prefix_sum[i]+suffix_sum[i] for i in range(n)]