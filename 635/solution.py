class LogSystem:

    def __init__(self):
        self.logs = {}

    def put(self, id: int, timestamp: str) -> None:
        self.logs[timestamp] = id

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        if gra == 'Year':
            start, end = 0, 4
        elif gra == 'Month':
            start, end = 5, 7
        elif gra == 'Day':
            start, end = 8, 10
        elif gra == 'Hour':
            start, end = 11, 13
        elif gra == 'Minute':
            start, end = 14, 16
        else:
            start, end = 17, 19
        start, end = s[:end], e[:end]
        return [self.logs[key] for key in self.logs if start <= key[:end] <= end]