class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        cur = sum([num for num in nums if num % 2 == 0])
        ans = []
        for (val, index) in queries:
            if nums[index] % 2 == 0:
                cur -= nums[index]
                
            nums[index] += val
            
            if nums[index] % 2 == 0:
                cur += nums[index]
                
            ans.append(cur)
            
        return ans