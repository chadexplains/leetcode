class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        heap = [(sum(row[0] for row in mat), [0] * len(mat))]
        seen = set(tuple([0] * len(mat)))
        for _ in range(k - 1):
            s, indices = heappop(heap)
            for i, index in enumerate(indices):
                if index + 1 < len(mat[i]):
                    new_indices = list(indices)
                    new_indices[i] += 1
                    if tuple(new_indices) not in seen:
                        seen.add(tuple(new_indices))
                        heappush(heap, (s - mat[i][index] + mat[i][index + 1], new_indices))
        return heap[0][0]