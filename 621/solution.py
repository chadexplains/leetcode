def leastInterval(self, tasks: List[str], n: int) -> int:
    freq = collections.Counter(tasks)
    max_freq = max(freq.values())
    max_freq_tasks = sum(1 for f in freq.values() if f == max_freq)
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_tasks)