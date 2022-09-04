from queue import Queue

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        queue = Queue()
        
        for i in range(1, 10):
            queue.put((i, i, 1))
            
        while not queue.empty():
            val, last, digit = queue.get()
            
            if digit == n:
                ans.append(val)
                continue
            
            if last - k >= 0:
                queue.put((val * 10 + last - k, last - k, digit + 1))
                
            if k > 0 and last + k <= 9:
                queue.put((val * 10 + last + k, last + k, digit + 1))
                
        return ans