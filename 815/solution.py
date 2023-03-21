class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        queue = deque([(S, 0)])
        visited = set([S])
        while queue:
            stop, buses = queue.popleft()
            if stop == T:
                return buses
            for route in stop_to_routes[stop]:
                for next_stop in routes[route]:
                    if next_stop not in visited:
                        visited.add(next_stop)
                        queue.append((next_stop, buses + 1))
                routes[route] = []
        return -1