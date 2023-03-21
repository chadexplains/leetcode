class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        possible_costs = set(baseCosts)
        for topping in toppingCosts:
            new_costs = set()
            for cost in possible_costs:
                new_costs.add(cost)
                new_costs.add(cost + topping)
                new_costs.add(cost + 2 * topping)
            possible_costs = new_costs
        closest_cost = float('inf')
        for cost in possible_costs:
            if abs(cost - target) < abs(closest_cost - target):
                closest_cost = cost
            elif abs(cost - target) == abs(closest_cost - target):
                closest_cost = min(closest_cost, cost)
        return closest_cost