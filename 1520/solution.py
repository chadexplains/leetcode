class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        char_dict = {}
        for i, c in enumerate(s):
            if c not in char_dict:
                char_dict[c] = [i, i]
            else:
                char_dict[c][1] = i
        intervals = []
        for c in char_dict:
            start, end = char_dict[c]
            i = start
            while i <= end:
                new_start, new_end = char_dict[s[i]]
                if new_start < start:
                    start = new_start
                    i = start
                if new_end > end:
                    end = new_end
                i += 1
            intervals.append([start, end])
        intervals.sort(key=lambda x: x[1])
        res = []
        end = -1
        for start, new_end in intervals:
            if start > end:
                res.append(s[start:new_end+1])
                end = new_end
        return res
