def findMaximizedCapital(k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
    available_projects = []
    for i in range(len(Profits)):
        available_projects.append((Profits[i], Capital[i]))
    available_projects.sort(reverse=True)
    completed_projects = []
    total_capital = W
    total_profit = 0
    while k > 0 and available_projects:
        while available_projects and available_projects[-1][1] > total_capital:
            completed_projects.append(available_projects.pop())
        if not available_projects:
            break
        project = available_projects.pop()
        total_profit += project[0]
        total_capital += project[1]
        k -= 1
    for project in completed_projects:
        heapq.heappush(available_projects, (-project[0], project[1]))
    return total_capital + total_profit