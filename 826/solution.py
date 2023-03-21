def maxProfitAssignment(difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    jobs = sorted(zip(difficulty, profit))
    worker.sort()
    i = max_profit = 0
    for ability in sorted(worker):
        while i < len(jobs) and ability >= jobs[i][0]:
            max_profit = max(max_profit, jobs[i][1])
            i += 1
    return max_profit