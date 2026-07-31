class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        maxHeap=stones
        heapq.heapify(maxHeap)
        while len(maxHeap)>=2:
            largest=-heapq.heappop(maxHeap)
            second=-heapq.heappop(maxHeap)
            if largest!=second:
                diff=largest-second
                heapq.heappush(maxHeap, -diff)
        if not maxHeap:
            return 0
        else:
            return -maxHeap[0]
        