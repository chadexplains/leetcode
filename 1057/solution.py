class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        for i, (wx, wy) in enumerate(workers):
            distances.append([])
            for j, (bx, by) in enumerate(bikes):
                distance = abs(wx - bx) + abs(wy - by)
                distances[-1].append((distance, i, j))
            distances[-1].sort()
        assigned_bikes = set()
        assigned_workers = set()
        heap = []
        for i in range(len(workers) * len(bikes)):
            distance, worker, bike = distances[i // len(bikes)][i % len(bikes)]
            if bike not in assigned_bikes and worker not in assigned_workers:
                assigned_bikes.add(bike)
                assigned_workers.add(worker)
                heap.append((bike, worker))
            if len(assigned_bikes) == len(bikes):
                break
        heap.sort(key=lambda x: x[1])
        return [x[0] for x in heap]