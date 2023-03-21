def bst_depth(insertions):
    depth = {}
    max_depth = 0
    for num in insertions:
        if num not in depth:
            parent_depth = depth.get(num // 2, 0)
            depth[num] = parent_depth + 1
            max_depth = max(max_depth, depth[num])
    return max_depth