def minKBitFlips(A: List[int], K: int) -> int:
    queue = deque()
    flips = 0
    left = right = 0
    max_len = 0
    while right < len(A):
        if A[right] == 0:
            if queue and left == queue[0]:
                queue.popleft()
                flips -= 1
            else:
                A[right] = 1
                queue.append(right + K - 1)
                flips += 1
        right += 1
        if flips > K:
            A[left] = 0
            left += 1
            flips -= 1
        max_len = max(max_len, right - left)
    return max_len