def findReplaceString(s, indices, sources, targets):
    mapping = {}
    for i in range(len(indices)):
        mapping[indices[i]] = (sources[i], targets[i])
    indices.sort(reverse=True)
    for index in indices:
        source, target = mapping[index]
        if s[index:index+len(source)] == source:
            s = s[:index] + target + s[index+len(source):]
    return s