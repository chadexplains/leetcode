def findCenter(edges):
    freq = {}
    n = len(edges)
    for edge in edges:
        freq[edge[0]] = freq.get(edge[0], 0) + 1
        freq[edge[1]] = freq.get(edge[1], 0) + 1
    for node, f in freq.items():
        if f == n:
            return node