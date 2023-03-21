```def eliminateMaximum(dist: List[int], speed: List[int]) -> int:
    monsters = [(dist[i], math.ceil(dist[i]/speed[i])) for i in range(len(dist))]
    monsters.sort(key=lambda x: (x[0], -x[1]))
    count = 0
    for i in range(len(monsters)):
        if monsters[i][1] > i:
            count += 1
        else:
            break
    return count```