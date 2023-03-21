class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        cells = [(i, j) for i in range(R) for j in range(C)]
        cells.sort(key=lambda cell: abs(cell[0] - r0) + abs(cell[1] - c0))
        return cells