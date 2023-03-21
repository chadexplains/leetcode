def mostCompetitive(nums: List[int], k: int) -> List[int]:
    stack = []
    for i, num in enumerate(nums):
        while stack and stack[-1] > num and len(stack) - 1 + len(nums) - i >= k:
            stack.pop()
        if len(stack) < k:
            stack.append(num)
    return stack