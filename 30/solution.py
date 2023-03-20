class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        n, m, k = len(s), len(words), len(words[0])
        if n < m * k:
            return []
        res = []
        dic = {}
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        for i in range(k):
            left = i
            sub_dic = {}
            count = 0
            for j in range(i, n-k+1, k):
                tword = s[j:j+k]
                if tword in dic:
                    sub_dic[tword] = sub_dic.get(tword, 0) + 1
                    count += 1
                    while sub_dic[tword] > dic[tword]:
                        sub_dic[s[left:left+k]] -= 1
                        left += k
                        count -= 1
                    if count == m:
                        res.append(left)
                        sub_dic[s[left:left+k]] -= 1
                        left += k
                        count -= 1
                else:
                    left = j + k
                    sub_dic = {}
                    count = 0
        return res