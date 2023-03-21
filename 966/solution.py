class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_set = set(wordlist)
        lower_dict = {}
        vowel_dict = {}
        for word in wordlist:
            lower = word.lower()
            vowel = re.sub('[aeiou]', '*', lower)
            lower_dict.setdefault(lower, word)
            vowel_dict.setdefault(vowel, word)
        res = []
        for query in queries:
            if query in word_set:
                res.append(query)
                continue
            lower = query.lower()
            if lower in lower_dict:
                res.append(lower_dict[lower])
                continue
            vowel = re.sub('[aeiou]', '*', lower)
            if vowel in vowel_dict:
                res.append(vowel_dict[vowel])
                continue
            res.append("")
        return res