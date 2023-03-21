def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    start, total_gas, total_cost, cum_sum = 0, 0, 0, 0
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        cum_sum += gas[i] - cost[i]
        if cum_sum < 0:
            start = i + 1
            cum_sum = 0
    return start if total_gas >= total_cost else -1