class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        last_rain = {}
        dry_days = []
        res = [-1] * len(rains)
        for i, r in enumerate(rains):
            if r == 0:
                dry_days.append(i)
                res[i] = 1
            else:
                if r in last_rain:
                    idx = bisect.bisect_left(dry_days, last_rain[r])
                    if idx == len(dry_days):
                        return []
                    res[dry_days[idx]] = r
                    dry_days.pop(idx)
                last_rain[r] = i
        for i in range(len(res)):
            if res[i] == -1:
                res[i] = 1
        return res