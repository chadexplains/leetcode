def daysBetweenDates(self, date1: str, date2: str) -> int:
    def julian(date):
        year, month, day = map(int, date.split('-'))
        if month < 3:
            year -= 1
            month += 12
        return 365 * year + year // 4 - year // 100 + year // 400 + (153 * month - 457) // 5 + day - 306
    return abs(julian(date1) - julian(date2))