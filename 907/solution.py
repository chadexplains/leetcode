class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = [0] * n, [0] * n
        stack1, stack2 = [], []
        for i in range(n):
            while stack1 and arr[stack1[-1]] > arr[i]:
                stack1.pop()
            left[i] = stack1[-1] if stack1 else -1
            stack1.append(i)
        for i in range(n - 1, -1, -1):
            while stack2 and arr[stack2[-1]] >= arr[i]:
                stack2.pop()
            right[i] = stack2[-1] if stack2 else n
            stack2.append(i)
        return sum((arr[i] * (i - left[i]) * (right[i] - i)) % (10**9 + 7) for i in range(n)) % (10**9 + 7)