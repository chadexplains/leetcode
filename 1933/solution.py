class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        count = 0
        curr_height = 0
        for i in range(len(rungs)):
            if rungs[i] - curr_height > dist:
                count += (rungs[i] - curr_height - 1) // dist
            curr_height = rungs[i]
        return count