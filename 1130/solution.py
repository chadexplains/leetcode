class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        cost = 0
        for num in arr:
            while stack[-1] <= num:
                cost += stack.pop() * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            cost += stack.pop() * stack[-1]
        return cost