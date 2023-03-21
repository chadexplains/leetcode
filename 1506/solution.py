def getLastMoment(n: int, left: List[int], right: List[int]) -> int:
    return max(n - min(left or [n]) , max(right or [0]))