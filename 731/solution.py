class MyCalendarTwo:

    def __init__(self):
        self.events = collections.OrderedDict()

    def book(self, start: int, end: int) -> bool:
        self.events[start] = self.events.get(start, 0) + 1
        self.events[end] = self.events.get(end, 0) - 1
        count = 0
        for time in self.events:
            count += self.events[time]
            if count >= 3:
                self.events[start] = self.events[start] - 1
                self.events[end] = self.events[end] + 1
                if self.events[start] == 0:
                    del self.events[start]
                if self.events[end] == 0:
                    del self.events[end]
                return False
        return True