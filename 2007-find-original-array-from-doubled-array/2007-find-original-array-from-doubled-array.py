class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        idx = 0
        ans = []
        
        for i in sorted(changed):
            if idx < len(ans):
                if 2 * ans[idx] == i:
                    idx += 1
                    continue
                    
            ans.append(i)
            
        if idx != len(ans):
            return []
        
        return ans
        
                    
                
            