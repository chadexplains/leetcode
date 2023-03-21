def twoCitySchedCost(costs):
    diffs = [(i, costs[i][0] - costs[i][1]) for i in range(len(costs))]
    diffs.sort(key=lambda x: x[1])
    total_cost = 0
    for i in range(len(costs)):
        if i < len(costs) // 2:
            total_cost += costs[diffs[i][0]][0]
        else:
            total_cost += costs[diffs[i][0]][1]
    return total_cost