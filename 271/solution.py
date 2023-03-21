class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)).zfill(5) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded