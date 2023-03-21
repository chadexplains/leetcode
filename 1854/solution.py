def maximumPopulation(self, logs: List[List[int]]) -> int:
    years = [0] * 101
    for log in logs:
        for i in range(log[0] - 1950, log[1] - 1950):
            years[i] += 1
    return years.index(max(years)) + 1950