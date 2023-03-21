class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_rings = min(m, n) // 2
        for ring in range(num_rings):
            num_elements = 2 * (m + n - 4 * ring) - 4
            elements = []
            for i in range(ring, m - ring):
                elements.append(grid[i][ring])
            for j in range(ring + 1, n - ring - 1):
                elements.append(grid[m - ring - 1][j])
            for i in range(m - ring - 1, ring - 1, -1):
                elements.append(grid[i][n - ring - 1])
            for j in range(n - ring - 2, ring - 1, -1):
                elements.append(grid[ring][j])
            rotated_elements = elements[-k % num_elements:] + elements[:-k % num_elements]
            index = 0
            for i in range(ring, m - ring):
                grid[i][ring] = rotated_elements[index]
                index += 1
            for j in range(ring + 1, n - ring - 1):
                grid[m - ring - 1][j] = rotated_elements[index]
                index += 1
            for i in range(m - ring - 1, ring - 1, -1):
                grid[i][n - ring - 1] = rotated_elements[index]
                index += 1
            for j in range(n - ring - 2, ring - 1, -1):
                grid[ring][j] = rotated_elements[index]
                index += 1
        return grid