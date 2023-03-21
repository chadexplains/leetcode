class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(a,b,c,d,e,f,g,h,i):
            return (sorted([a,b,c,d,e,f,g,h,i]) == list(range(1, 10)) and
                    (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15))
        ans = 0
        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                if isMagic(*grid[r][c:c+3], *grid[r+1][c:c+3], *grid[r+2][c:c+3]):
                    ans += 1
        return ans