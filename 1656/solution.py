class OrderedStream:
    
    def __init__(self, n: int):
        self.stream = [None] * n
        self.next_id = 1
        self.buffer = []

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id-1] = value
        if id == self.next_id:
            result = []
            while id-1 < len(self.stream) and self.stream[id-1] is not None:
                result.append(self.stream[id-1])
                id += 1
            self.next_id = id
            if self.buffer:
                result += self.add_buffered_chunks()
            return result
        else:
            self.buffer.append((id, value))
            return []

    def add_buffered_chunks(self) -> List[str]:
        result = []
        while self.buffer and self.buffer[0][0] == self.next_id:
            result.append(self.buffer.pop(0)[1])
            self.next_id += 1
        return result