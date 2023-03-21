class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rungs.insert(0, 0)
        num_rungs_added = 0
        for i in range(1, len(rungs)):
            if rungs[i] - rungs[i-1] > dist:
                num_rungs_added += (rungs[i] - rungs[i-1] - 1) // dist
        return num_rungs_added