def longestSubstring(s: str, k: int) -> int:
    if len(s) < k:
        return 0
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] < k:
            return max(longestSubstring(s[:i], k), longestSubstring(s[i+1:], k))
    return len(s)