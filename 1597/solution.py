def minOperationsMaxProfit(customers: List[int], boardingCost: int, runningCost: int) -> int:
    waiting = 0
    rotations = 0
    max_profit = -1
    profit = 0
    queue = []
    for i, c in enumerate(customers):
        waiting += c
        if waiting > 4:
            queue.append(waiting - 4)
            waiting = 4
        profit += min(waiting, 4) * boardingCost - runningCost
        if profit > max_profit:
            max_profit = profit
            rotations = i + 1
        if not queue and waiting == 0:
            break
        waiting -= min(waiting, 4)
        waiting += queue.pop(0) if queue else 0
    return rotations if max_profit > 0 else -1