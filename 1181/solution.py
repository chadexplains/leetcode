class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        words = [phrase.split() for phrase in phrases]
        output = set()
        for i in range(len(phrases)):
            for j in range(len(phrases)):
                if i != j and words[i][-1] == words[j][0]:
                    output.add(' '.join(words[i] + words[j][1:]))
        return sorted(output)