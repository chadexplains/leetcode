def wordPatternMatch(pattern: str, s: str) -> bool:
    def backtrack(pattern, s, p2s, s2p):
        if not pattern and not s:
            return True
        if not pattern or not s:
            return False
        for i in range(1, len(s) - len(pattern) + 2):
            p, ss = pattern[0], s[:i]
            if p in p2s and p2s[p] != ss:
                continue
            if ss in s2p and s2p[ss] != p:
                continue
            p2s[p], s2p[ss] = ss, p
            if backtrack(pattern[1:], s[i:], p2s, s2p):
                return True
            del p2s[p], s2p[ss]
        return False
    return backtrack(pattern, s, {}, {})