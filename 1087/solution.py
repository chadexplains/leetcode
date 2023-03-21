class Solution:
    def expand(self, s: str) -> List[str]:
        def backtrack(combination, index):
            if index == len(options):
                result.append(combination)
                return
            for option in options[index]:
                backtrack(combination + option, index + 1)
        options = []
        i = 0
        while i < len(s):
            if s[i] == '{':
                j = i + 1
                while s[j] != '}':
                    j += 1
                options.append(sorted(s[i+1:j].split(',')))
                i = j + 1
            else:
                options.append([s[i]])
                i += 1
        result = []
        backtrack('', 0)
        return sorted(result)