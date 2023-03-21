def restaurantGrowth(logs: List[str]) -> List[int]:
    counts = {}
    for log in logs:
        year, count = log.split()
        if year not in counts:
            counts[year] = 1
        else:
            counts[year] += 1
    return list(counts.values())