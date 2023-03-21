class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 0:
                row += 1
            else:
                col -= 1
        return col + 1 if col < cols - 1 else -1