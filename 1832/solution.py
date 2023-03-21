class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = {}
        for c in sentence:
            letters[c] = True
            if len(letters) == 26:
                return True
        return False