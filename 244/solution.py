class WordDistance:
    
    def __init__(self, words: List[str]):
        self.word_dict = {}
        for i, word in enumerate(words):
            if word in self.word_dict:
                self.word_dict[word].append(i)
            else:
                self.word_dict[word] = [i]

    def shortest(self, word1: str, word2: str) -> int:
        indices1 = self.word_dict[word1]
        indices2 = self.word_dict[word2]
        i = j = 0
        min_distance = float('inf')
        while i < len(indices1) and j < len(indices2):
            min_distance = min(min_distance, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1
        return min_distance