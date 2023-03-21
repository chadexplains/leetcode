class Solution:
    def checkRecord(self, s: str) -> bool:
        absences = 0
        continuous_late_days = 0
        for c in s:
            if c == 'A':
                absences += 1
                continuous_late_days = 0
                if absences > 1:
                    return False
            elif c == 'L':
                continuous_late_days += 1
                if continuous_late_days > 2:
                    return False
            else:
                continuous_late_days = 0
        return True