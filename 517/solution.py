def findMinMoves(machines):
    total = sum(machines)
    n = len(machines)
    if total % n != 0:
        return -1
    avg = total // n
    moves = 0
    left = 0
    right = total
    for i in range(n):
        right -= machines[i]
        right_avg = (right - left) // (n - i - 1) if i < n - 1 else 0
        left_avg = (left - right_avg - avg * i) // i if i > 0 else 0
        diff = machines[i] - avg
        if diff > 0:
            moves = max(moves, diff - min(right_avg, diff))
        elif diff < 0:
            moves = max(moves, abs(diff) - min(left_avg, abs(diff)))
        left += machines[i]
    return moves