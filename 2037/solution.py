def minOperations(boxes):
    n = len(boxes)
    prefix_sum = [0]*n
    suffix_sum = [0]*n
    balls_seen = 0
    for i in range(n):
        prefix_sum[i] = balls_seen
        if boxes[i] == '1':
            balls_seen += 1
    balls_seen = 0
    for i in range(n-1, -1, -1):
        suffix_sum[i] = balls_seen
        if boxes[i] == '1':
            balls_seen += 1
    return [prefix_sum[i] + suffix_sum[i] for i in range(n)]