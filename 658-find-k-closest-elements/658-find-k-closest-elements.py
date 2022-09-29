class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo = list(reversed([a for a in arr if a <= x]))
        hi = [a for a in arr if a > x]
        
        merge = []
        i, j = 0, 0
        for _ in range(k):
            takeL = True
            
            if i < len(lo) and j < len(hi):
                takeL = (x - lo[i]) <= (hi[j] - x)
            elif i < len(lo):
                takeL = True
            elif j < len(hi):
                takeL = False
            else:
                break      
                
            if takeL:
                i += 1
            else:
                j += 1
        
        return list(reversed(lo[:i])) + hi[:j]
            