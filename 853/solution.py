class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        curr_time = -1
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > curr_time:
                fleets += 1
                curr_time = time
        return fleets