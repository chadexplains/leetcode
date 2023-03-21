class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = {}
        res = []
        for name in names:
            if name not in used:
                used[name] = 0
                res.append(name)
            else:
                used[name] += 1
                new_name = name + "(" + str(used[name]) + ")"
                while new_name in used:
                    used[name] += 1
                    new_name = name + "(" + str(used[name]) + ")"
                used[new_name] = 0
                res.append(new_name)
        return res