class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        language_dict = {}
        for i, lang in enumerate(languages):
            language_dict[i+1] = set(lang)
        to_teach = set()
        for a, b in friendships:
            if not language_dict[a] & language_dict[b]:
                to_teach.add(a)
                to_teach.add(b)
        lang_count = Counter()
        for person in to_teach:
            for lang in language_dict[person]:
                lang_count[lang] += 1
        if not lang_count:
            return 0
        lang, count = lang_count.most_common()[0]
        taught = set()
        for person in to_teach:
            if lang not in language_dict[person]:
                taught.add(person)
        return len(taught)