class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [None for _ in range(k)]
        self.capacity = k
        self.begin = 0
        self.size = 0
    
    def get_end(self):
        return (self.begin + self.size + self.capacity - 1) % self.capacity
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        pos = (self.get_end() + 1) % self.capacity
        self.data[pos] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.data[self.begin] = None
        self.begin = (self.begin + 1) % self.capacity
        self.size -= 1        
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        
        return self.data[self.begin]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        
        return self.data[self.get_end()]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()