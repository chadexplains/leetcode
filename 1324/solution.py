def printVertically(s):
    words = s.split()
    max_len = max(len(w) for w in words)
    output = [' ' * len(words) for _ in range(max_len)]
    for i, word in enumerate(words):
        for j, char in enumerate(word):
            output[j] = output[j][:i] + char + output[j][i+1:]
    return [col.rstrip() for col in output]