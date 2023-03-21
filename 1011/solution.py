```def shipWithinDays(weights, D):
    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        days = 1
        total = 0
        for weight in weights:
            if total + weight > mid:
                days += 1
                total = 0
            total += weight
        if days <= D:
            right = mid
        else:
            left = mid + 1
    return left```