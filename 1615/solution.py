class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_matrix = [[0] * n for _ in range(n)]
        degrees = {}
        for i, j in roads:
            adj_matrix[i][j] = 1
            adj_matrix[j][i] = 1
        for i in range(n):
            degrees[i] = sum(adj_matrix[i])
        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = degrees[i] + degrees[j] - adj_matrix[i][j]
                max_rank = max(max_rank, rank)
        return max_rank