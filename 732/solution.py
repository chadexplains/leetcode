class MyCalendarThree:
    
    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.bookings, (start, 1))
        bisect.insort(self.bookings, (end, -1))
        max_overlaps = cur_overlaps = 0
        for _, delta in self.bookings:
            cur_overlaps += delta
            max_overlaps = max(max_overlaps, cur_overlaps)
        return max_overlaps