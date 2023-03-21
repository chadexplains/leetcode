def minOperations(boxes):
    prefix_sum = []
    count = 0
    for box in boxes:
        prefix_sum.append(count)
        count += int(box)
    suffix_sum = 0
    answer = []
    for box in reversed(boxes):
        answer.append(suffix_sum)
        suffix_sum += int(box)
    answer.reverse()
    for i in range(len(boxes)):
        answer[i] += prefix_sum[i]
        answer[i] += suffix_sum[i]
    return answer