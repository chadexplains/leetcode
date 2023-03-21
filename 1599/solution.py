class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        customers.append(0)
        rotations = 0
        max_profit = 0
        curr_profit = 0
        waiting = 0
        i = 0
        while i < n or waiting > 0:
            if i < n:
                waiting += customers[i]
            boarded = min(waiting, 4)
            waiting -= boarded
            curr_profit += boarded * boardingCost - runningCost
            rotations += 1
            if curr_profit > max_profit:
                max_profit = curr_profit
                res = rotations
            i += 1
        return res if max_profit > 0 else -1