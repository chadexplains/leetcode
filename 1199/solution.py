class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        pq = blocks[:split]
        heapq.heapify(pq)
        for i in range(split, len(blocks)):
            t = heapq.heappop(pq)
            heapq.heappush(pq, t + blocks[i])
        return max(pq)