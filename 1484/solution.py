def getFolderNames(names):
    freq = {}
    result = []
    for name in names:
        if name not in freq:
            freq[name] = 1
            result.append(name)
        else:
            k = freq[name]
            while f'{name}({k})' in freq:
                k += 1
            freq[name] = k
            freq[f'{name}({k})'] = 1
            result.append(f'{name}({k})')
    return result