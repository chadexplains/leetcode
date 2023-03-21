class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"\w+", paragraph.lower())
        freq = collections.Counter(words)
        for word in banned:
            freq.pop(word, None)
        return freq.most_common(1)[0][0]