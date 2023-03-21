class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def binary_search(lo, hi, check, get):
            while lo < hi:
                mid = (lo + hi) // 2
                if check(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        m, n = len(image), len(image[0])
        row = binary_search(0, x, lambda x: '1' in image[x], lambda x: x)
        row2 = binary_search(x, m, lambda x: '1' not in image[x], lambda x: x - 1)
        col = binary_search(0, y, lambda y: any(image[i][y] == '1' for i in range(m)), lambda y: y)
        col2 = binary_search(y, n, lambda y: all(image[i][y] == '0' for i in range(m)), lambda y: y - 1)
        return (row2 - row + 1) * (col2 - col + 1)