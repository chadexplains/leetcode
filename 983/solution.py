def mincostTickets(days, costs):
    travel_days = set(days)
    min_cost = [0] * 366
    for i in range(1, 366):
        if i not in travel_days:
            min_cost[i] = min_cost[i-1]
        else:
            min_cost[i] = min(min_cost[i-1] + costs[0], min_cost[max(0, i-7)] + costs[1], min_cost[max(0, i-30)] + costs[2])
    return min_cost[365]