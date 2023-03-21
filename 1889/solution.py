class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        total_waste = float('inf')
        for box in boxes:
            box.sort()
            if box[-1] < packages[-1]:
                continue
            waste = i = 0
            for p in packages:
                j = bisect_right(box, p, i)
                waste += (j-i) * p
                i = j
                if i == len(box):
                    break
            if i < len(box):
                continue
            total_waste = min(total_waste, waste)
        return -1 if total_waste == float('inf') else total_waste % (10**9 + 7)