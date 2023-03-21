class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        days_in_month = {1: 31, 2: 28 if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) else 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        total_days = sum(days_in_month[i] for i in range(1, month))
        total_days += day
        return total_days