class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        for region in regions:
            for i in range(1, len(region)):
                parent[region[i]] = region[0]
        path1 = [region1]
        while path1[-1] in parent:
            path1.append(parent[path1[-1]])
        path2 = [region2]
        while path2[-1] in parent:
            path2.append(parent[path2[-1]])
        path1.reverse()
        path2.reverse()
        i = 0
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
            i += 1
        return path1[i-1]