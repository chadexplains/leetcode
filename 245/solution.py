def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
    p1 = p2 = -1
    min_distance = float('inf')
    for i, word in enumerate(wordsDict):
        if word == word1:
            p1 = i
        if word == word2:
            p2 = i
        if p1 != -1 and p2 != -1:
            if word1 == word2:
                p1 = p2
            min_distance = min(min_distance, abs(p1 - p2))
    return min_distance