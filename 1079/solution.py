class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(curr, tiles, seen):
            if curr:
                seen.add(curr)
            for i in range(len(tiles)):
                backtrack(curr + tiles[i], tiles[:i] + tiles[i+1:], seen)
        seen = set()
        backtrack('', tiles, seen)
        return len(seen)