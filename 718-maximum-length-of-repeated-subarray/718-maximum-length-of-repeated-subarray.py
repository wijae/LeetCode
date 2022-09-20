class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        
        ans = 0
        for d in range(-(n-1), n):
            cur = 0
            
            for i in range(m):
                if 0 <= i+d and i+d < n:
                    if nums1[i+d] == nums2[i]:
                        cur += 1
                    else:
                        cur = 0
                        
                    if ans < cur:
                        ans = cur
                    
        return ans
        