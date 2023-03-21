def gardenNoAdj(N, paths):
    graph = [[] for _ in range(N)]
    for x, y in paths:
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
    flowers = [0] * N
    for i in range(N):
        used = set(flowers[j] for j in graph[i])
        for color in range(1, 5):
            if color not in used:
                flowers[i] = color
                break
    return flowers