class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for i in range(len(classes)):
            pass_ratio = classes[i][0] / classes[i][1]
            heapq.heappush(heap, (-((pass_ratio + 1) / (classes[i][1] + 1) - pass_ratio), i))
        while extraStudents > 0:
            _, i = heapq.heappop(heap)
            classes[i][0] += 1
            classes[i][1] += 1
            pass_ratio = classes[i][0] / classes[i][1]
            heapq.heappush(heap, (-((pass_ratio + 1) / (classes[i][1] + 1) - pass_ratio), i))
            extraStudents -= 1
        return sum([c[0] / c[1] for c in classes]) / len(classes)