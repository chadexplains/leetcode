class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = {k: v for k, v in knowledge}
        result = ""
        i = 0
        while i < len(s):
            if s[i] == "(":
                j = i + 1
                while s[j] != ")":
                    j += 1
                key = s[i+1:j]
                if key in knowledge_dict:
                    result += knowledge_dict[key]
                else:
                    result += "?"
                i = j + 1
            else:
                result += s[i]
                i += 1
        return result