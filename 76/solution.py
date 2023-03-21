class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = collections.Counter(t)
        left = 0
        right = 0
        count = len(t)
        min_window = float('inf')
        min_window_start = 0
        while right < len(s):
            if s[right] in freq:
                if freq[s[right]] > 0:
                    count -= 1
                freq[s[right]] -= 1
            right += 1
            while count == 0:
                if right - left < min_window:
                    min_window = right - left
                    min_window_start = left
                if s[left] in freq:
                    freq[s[left]] += 1
                    if freq[s[left]] > 0:
                        count += 1
                left += 1
        return '' if min_window == float('inf') else s[min_window_start:min_window_start+min_window]