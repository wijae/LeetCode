class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        for c in magazine:
            if c not in chars:
                chars[c] = 0
            
            chars[c] += 1
            
        for c in ransomNote:
            if c not in chars or chars[c] == 0:
                return False
            
            chars[c] -= 1
            
        return True
        