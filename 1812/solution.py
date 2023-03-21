class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        row = int(coordinates[1])
        col = ord(coordinates[0]) - ord('a') + 1
        return (row + col) % 2 == 0