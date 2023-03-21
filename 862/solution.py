def shortestSubarray(self, A: List[int], K: int) -> int:
    n = len(A)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + A[i]
    deque = collections.deque()
    deque.append((0, 0))
    min_length = float('inf')
    for i in range(1, n + 1):
        while deque and prefix_sum[i] - deque[0][1] >= K:
            min_length = min(min_length, i - deque[0][0])
            deque.popleft()
        while deque and prefix_sum[i] <= deque[-1][1]:
            deque.pop()
        deque.append((i, prefix_sum[i]))
    return min_length if min_length != float('inf') else -1