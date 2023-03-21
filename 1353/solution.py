class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        days_attended = set()
        count = 0
        for event in events:
            for day in range(event[0], event[1] + 1):
                if day not in days_attended:
                    days_attended.add(day)
                    count += 1
                    break
        return count