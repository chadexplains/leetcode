def largestValsFromLabels(values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
    items = [(values[i], labels[i]) for i in range(len(values))]
    items.sort(reverse=True)
    selected = {}
    subset = []
    for value, label in items:
        if label not in selected:
            selected[label] = 0
        if selected[label] < use_limit:
            subset.append(value)
            selected[label] += 1
        if len(subset) == num_wanted:
            break
    return sum(subset)