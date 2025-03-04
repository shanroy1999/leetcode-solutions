class MedianFinder:

    def __init__(self):
        # self.arr = []
        # Use 2 heaps => largeHeap (minHeap) and a smallHeap(maxHeap)
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        # self.arr.append(num)
        # smallHeap -> is the MaxHeap
        # largeHeap -> is the MinHeap
        heapq.heappush(self.smallHeap, -1 * num)

        # Make sure every value in smallHeap is < every value in largeHeap
        if (self.smallHeap and self.largeHeap and (-1 * self.smallHeap[0]) > self.largeHeap[0]):
            # If some value in smallHeap > min value of LargeHeap
            # Pop that value from the smallHeap and push it into the LargeHeap
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)
        
        # Check if the size is uneven 
        # difference in length of smallHeap and largeHeap > 1
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        if len(self.largeHeap) > len(self.smallHeap) + 1:
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1*val)

    def findMedian(self) -> float:
        # left = 0
        # right = len(self.arr)-1
        # if len(self.arr)%2==0:
        #     # Even number of elements
        #     mid1 = (right-left)//2
        #     mid2 = (right-left)//2+1
        #     return (self.arr[mid1]+self.arr[mid2])/2
        # else:
        #     return self.arr[(right-left)//2]

        if len(self.smallHeap) > len(self.largeHeap):
            # Odd number of elements => smallHeap has an extra element
            # Median = largest value in the smallHeap (MaxHeap)
            return -1*self.smallHeap[0]
        if len(self.largeHeap) > len(self.smallHeap):
            # Odd number of elements => largeHeap has an extra element
            # Median = smallest value in the largeHeap (MaxHeap)
            return self.largeHeap[0]
        # Even number of elements
        # Median = mean of (smallest value of largeHeap) and the (largest value of smallHeap)
        return (-1*self.smallHeap[0] + self.largeHeap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()