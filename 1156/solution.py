def maxRepOpt1(text):
    counts = collections.Counter(text)
    max_len = 1
    for i in range(len(text)):
        char = text[i]
        count = 1
        j = i + 1
        while j < len(text) and (text[j] == char or count < counts[char]):
            if text[j] != char:
                count += 1
            j += 1
        if count == counts[char] and j < len(text) and text[j] == char:
            count += 1
        max_len = max(max_len, count)
    return max_len