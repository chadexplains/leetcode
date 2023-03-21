class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]
                customers[i] = 0
        max_additional_satisfied = 0
        additional_satisfied = 0
        for i in range(n):
            additional_satisfied += customers[i]
            if i >= X:
                additional_satisfied -= customers[i - X]
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        return satisfied + max_additional_satisfied