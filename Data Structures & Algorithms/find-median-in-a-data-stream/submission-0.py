import heapq


class MedianFinder:

    def __init__(self):
        # Max-heap (stores smaller half, negated for max-heap behavior)
        self.small = []
        # Min-heap (stores larger half)
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Add to max-heap
        heapq.heappush(self.small, -num)

        # Step 2: Transfer largest of small half to min-heap
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 3: Rebalance sizes (small can have 1 more element than large)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0