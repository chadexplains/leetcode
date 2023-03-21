class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        new_event = Interval(start, end)
        for event in self.events:
            if new_event.start < event.end and event.start < new_event.end:
                return False
        self.events.append(new_event)
        return True