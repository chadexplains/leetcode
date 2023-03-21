def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
    m = len(rolls)
    total_sum = sum(rolls)
    target_sum = (n + m) * mean
    missing_sum = target_sum - total_sum
    if missing_sum < n or missing_sum > 6 * n:
        return []
    missing_avg = missing_sum / n
    missing = [missing_avg] * n
    for i in range(missing_sum % n):
        missing[i] += 1
    return missing