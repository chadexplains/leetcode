class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word_dict = {}
        for i, word in enumerate(words):
            if word not in word_dict:
                word_dict[word] = [i]
            else:
                word_dict[word].append(i)
        min_distance = len(words)
        for i in word_dict[word1]:
            for j in word_dict[word2]:
                min_distance = min(min_distance, abs(i-j))
        return min_distance