class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used_names = set()
        result = []
        for name in names:
            if name not in used_names:
                used_names.add(name)
                result.append(name)
            else:
                k = 1
                new_name = name + "(" + str(k) + ")"
                while new_name in used_names:
                    k += 1
                    new_name = name + "(" + str(k) + ")"
                used_names.add(new_name)
                result.append(new_name)
        return result