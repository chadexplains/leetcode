class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = sorted(set(time))
        hh, mm = time.split(':')
        while True:
            mm = str((int(mm) + 1) % 60).zfill(2)
            if mm == '00':
                hh = str((int(hh) + 1) % 24).zfill(2)
            new_time = hh + ':' + mm
            if all(digit in digits for digit in new_time):
                return new_time