class Leaderboard:
    
    def __init__(self):
        self.scores = {}
        self.heap = []
        heapq.heapify(self.heap)
        
    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            self.heap.remove(-self.scores[playerId])
        self.scores[playerId] = score
        heapq.heappush(self.heap, -score)
        
    def top(self, K: int) -> int:
        res = 0
        for i in range(K):
            if self.heap:
                res -= heapq.heappop(self.heap)
        for score in self.heap:
            res += score
        return res
        
    def reset(self) -> None:
        self.scores = {}
        self.heap = []
        heapq.heapify(self.heap)