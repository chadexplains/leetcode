class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        start = (int(startTime[:2]) * 60 + int(startTime[3:]))
        end = (int(finishTime[:2]) * 60 + int(finishTime[3:]))
        if start > end:
            end += 24 * 60
        start = (start + 14) // 15 * 15
        end = end // 15 * 15
        return max(0, (end - start) // 15)
