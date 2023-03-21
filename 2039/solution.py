def minOperations(boxes):
    prefix_sum = []
    current_sum = 0
    for i in range(len(boxes)):
        prefix_sum.append(current_sum)
        if boxes[i] == '1':
            current_sum += 1
    suffix_sum = []
    current_sum = 0
    for i in range(len(boxes)-1, -1, -1):
        suffix_sum.append(current_sum)
        if boxes[i] == '1':
            current_sum += 1
    suffix_sum.reverse()
    answer = []
    for i in range(len(boxes)):
        answer.append(prefix_sum[i] + suffix_sum[i])
    return answer