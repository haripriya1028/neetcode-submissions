class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        self.maxHeap=stones
        heapq.heapify(self.maxHeap)
        while len(self.maxHeap)>=2:
            largest=-heapq.heappop(self.maxHeap)
            second=-heapq.heappop(self.maxHeap)
            if largest!=second:
                diff=largest-second
                heapq.heappush(self.maxHeap, -diff)
        if not self.maxHeap:
            return 0
        else:
            return -self.maxHeap[0]
        