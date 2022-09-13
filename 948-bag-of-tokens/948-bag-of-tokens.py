class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        
        ans = 0
        score = 0
        while len(tokens) > 0:
            if power >= tokens[0]:
                power -= tokens[0]
                score += 1
                tokens = tokens[1:]
            elif score > 0:
                power += tokens[-1]
                score -= 1
                tokens = tokens[:-1]
            else:
                break
            
            if ans < score:
                ans = score
                
        return ans