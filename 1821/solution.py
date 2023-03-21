def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
    total_rolls = len(rolls) + n
    total_sum = mean * total_rolls
    given_sum = sum(rolls)
    missing_sum = total_sum - given_sum
    if missing_sum < n or missing_sum > n * 6:
        return []
    missing_avg, missing_remainder = divmod(missing_sum, n)
    return [missing_avg + (i < missing_remainder) for i in range(n)]