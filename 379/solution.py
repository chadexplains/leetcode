class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available = set(range(maxNumbers))
        self.released = collections.deque()
        
    def get(self) -> int:
        if self.released:
            num = self.released.popleft()
        elif self.available:
            num = self.available.pop()
        else:
            num = -1
        return num

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        if number not in self.available:
            self.available.add(number)
            self.released.append(number)