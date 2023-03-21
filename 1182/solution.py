```def shortestDistanceColor(colors: List[int], queries: List[List[int]]) -> List[int]:
    color_indices = defaultdict(list)
    for i, color in enumerate(colors):
        color_indices[color].append(i)
    answer = []
    for query in queries:
        color, index = query
        if color not in color_indices:
            answer.append(0)
        else:
            indices = color_indices[color]
            left = bisect_left(indices, index)
            if left == 0:
                answer.append(indices[0] - index)
            elif left == len(indices):
                answer.append(index - indices[-1])
            else:
                answer.append(min(indices[left] - index, index - indices[left-1]))
    return answer```