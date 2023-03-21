class Solution:
    def solve(self, words: List[str], result: str) -> List[str]:
        chars = set(''.join(words) + result)
        if len(chars) > 10:
            return []
        chars = list(chars)
        n = len(chars)
        used = [False] * 10
        mapping = {}
        res = []
        def backtrack(i, carry):
            nonlocal res
            if i == n:
                if carry == 0:
                    res.append(''.join([mapping[ch] for ch in result]))
                return
            for digit in range(10):
                if not used[digit]:
                    used[digit] = True
                    if i == len(words[-1]):
                        s = carry
                    else:
                        idx = len(words[-1]) - i - 1
                        if idx < len(words[0]):
                            s = int(mapping[words[0][idx]])
                        else:
                            s = 0
                        for j in range(1, len(words)):
                            if idx < len(words[j]):
                                s += int(mapping[words[j][len(words[j]) - idx - 1]])
                        s += carry
                    if s % 10 == digit:
                        mapping[chars[i]] = str(digit)
                        backtrack(i + 1, s // 10)
                        mapping.pop(chars[i])
                    used[digit] = False
        backtrack(0, 0)
        return res