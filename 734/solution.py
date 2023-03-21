class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        similar_words = {}
        for pair in pairs:
            if pair[0] not in similar_words:
                similar_words[pair[0]] = set()
            if pair[1] not in similar_words:
                similar_words[pair[1]] = set()
            similar_words[pair[0]].add(pair[1])
            similar_words[pair[1]].add(pair[0])
        for i in range(len(words1)):
            if words1[i] != words2[i] and words2[i] not in similar_words.get(words1[i], set()):
                return False
        return True