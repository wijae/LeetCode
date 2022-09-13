from queue import PriorityQueue

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        minus_efficiency_speed = sorted([(-efficiency[i], speed[i]) for i in range(n)])
        
        ans = 0
        speed_sum = 0
        speed_queue = PriorityQueue()
        
        for (minus_efficiency, speed) in minus_efficiency_speed:
            efficiency = -minus_efficiency
            
            speed_queue.put(speed)
            speed_sum += speed
            
            if speed_queue.qsize() > k:
                speed_sum -= speed_queue.get()
                
            if ans < speed_sum * efficiency:
                ans = speed_sum * efficiency
            
        return ans % (1000000007)