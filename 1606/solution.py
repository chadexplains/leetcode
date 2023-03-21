class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, i)
        busy_servers = []
        server_count = [0] * k
        for i in range(len(arrival)):
            while busy_servers and busy_servers[0][0] <= arrival[i]:
                _, server = heapq.heappop(busy_servers)
                heapq.heappush(heap, server)
            if not heap:
                continue
            server = heapq.heappop(heap)
            server_count[server] += 1
            heapq.heappush(busy_servers, (arrival[i] + load[i], server))
        return server_count