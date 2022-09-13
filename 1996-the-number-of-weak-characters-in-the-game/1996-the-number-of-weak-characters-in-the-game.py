class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        p = sorted([(-properties[i][0], properties[i][1]) for i in range(len(properties))])
        
        ans = 0
        max_defence = 0
        for (minus_attack, defence) in p:
            attack = -minus_attack
            
            print(attack, defence, max_defence)
        
            if defence < max_defence:
                ans += 1
            
            if max_defence < defence:
                max_defence = defence
                
        return ans