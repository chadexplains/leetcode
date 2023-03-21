```
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def timeTaken(speed):
            return sum(math.ceil(d / speed) for d in dist[:-1]) + dist[-1] / speed

        n = len(dist)
        min_speed, max_speed = 1, 10**7
        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            time = timeTaken(mid_speed)
            if time <= hour:
                min_speed = mid_speed + 1
            else:
                max_speed = mid_speed - 1
        return min_speed if min_speed <= 10**7 else -1
```