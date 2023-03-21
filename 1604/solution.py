class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        key_presses = {}
        for i in range(len(keyName)):
            if keyName[i] not in key_presses:
                key_presses[keyName[i]] = []
            key_presses[keyName[i]].append(int(keyTime[i].replace(':', '')))
        result = []
        for person in key_presses:
            key_presses[person].sort()
            for i in range(len(key_presses[person]) - 2):
                if key_presses[person][i + 2] - key_presses[person][i] <= 100:
                    result.append(person)
                    break
        return sorted(result)