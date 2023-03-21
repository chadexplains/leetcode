class Solution:
    def canWin(self, currentState: str) -> bool:
        for i in range(len(currentState) - 1):
            if currentState[i] == '+' and currentState[i+1] == '+':
                newState = currentState[:i] + '--' + currentState[i+2:]
                if not self.canWin(newState):
                    return True
        return False