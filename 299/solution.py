class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        freq = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                freq[int(secret[i])] += 1
        for i in range(len(guess)):
            if secret[i] != guess[i] and freq[int(guess[i])] > 0:
                cows += 1
                freq[int(guess[i])] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'