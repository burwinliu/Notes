class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []
        

    def addNum(self, num: int) -> None:
        if len(self.store) == 0:
            self.store.append(num)
            return
        left, right = 0, len(self.store)-1
        while right-left > 1:
            if num == 17:
                print(right, left, self.store)
            mid = (right-left)//2 + left 
            if self.store[mid] < num:
                left = mid
            elif self.store[mid] > num:
                right = mid
            else:
                self.store.insert(mid, num)
                return
        
        if num < self.store[left]:
            self.store.insert(left, num)
        elif num < self.store[right]:
            self.store.insert(right, num)
        elif num >= self.store[right]:
            self.store.insert(right+1, num)

    def findMedian(self) -> float:
        if len(self.store) % 2 == 0:
            return (self.store[len(self.store)//2] - self.store[(len(self.store)//2)-1])/2 + self.store[(len(self.store)//2)-1]
        else:
            return self.store[len(self.store)//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Seems to be a typical PQ/binary search esque (trade off a bit of time to sort values, use sturcture to derive meaning)