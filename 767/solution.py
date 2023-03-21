def reorganizeString(S):
    counts = collections.Counter(S)
    max_char = max(counts, key=counts.get)
    max_count = counts[max_char]
    if max_count > (len(S) + 1) // 2:
        return ""
    res = [""] * len(S)
    res[::2], res[1::2] = [max_char] * max_count, list(counts.elements())
    return "".join(res)