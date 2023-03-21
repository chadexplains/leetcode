class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = (N - 1) % 14 + 1
        for i in range(N):
            prev = cells[0]
            for j in range(1, 7):
                curr = cells[j]
                next = cells[j + 1]
                if prev == next:
                    cells[j] = 1
                else:
                    cells[j] = 0
                prev = curr
            cells[0], cells[7] = 0, 0
        return cells