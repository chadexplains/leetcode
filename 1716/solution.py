class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        current_day = 1
        current_week = 1
        for i in range(1, n+1):
            if current_day == 1:
                total += current_week
                current_week += 1
            else:
                total += current_day
            current_day += 1
            if current_day == 8:
                current_day = 1
        return total