class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        for f in sorted(folder):
            cur = trie
            for c in f.split('/')[1:]:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = {}
        res = []
        for f in folder:
            cur = trie
            flag = True
            for c in f.split('/')[1:]:
                if '#' in cur:
                    break
                if c not in cur:
                    flag = False
                    break
                cur = cur[c]
            if flag:
                res.append(f)
        return res
