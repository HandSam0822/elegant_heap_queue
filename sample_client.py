from source.heap_queue import HeapQueue, HeapType


class MedianFinder:

    def __init__(self):
        # smaller half of data. maxHeap[0] stores the biggest data in smaller half
        self.maxHeap = HeapQueue(heap_type=HeapType.MAX_HEAP)
        # bigger half of data. minHeap[0] stores the smallest data in bigger half
        self.minHeap = HeapQueue(heap_type=HeapType.MIN_HEAP)

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) > len(self.minHeap):
            self.maxHeap.push(num)
            x = self.maxHeap.pop()
            self.minHeap.push(x)
        else:
            self.minHeap.push(num)
            y = self.minHeap.pop()
            self.maxHeap.push(y)

    def findMedian(self) -> float:
        # if number of element is odd, median is biggest element in maxHeap
        if (len(self.maxHeap) + len(self.minHeap)) % 2 != 0:
            return (self.maxHeap.peek())
        # if number of element is even, median is the mean of greatest element in maxHeap and smallest element in minHeap
        return (self.maxHeap.peek() + self.minHeap.peek()) / 2

if __name__ == "__main__":
    finder = MedianFinder()
    finder.addNum(3.0)
    finder.addNum(1.1)
    finder.addNum(5.2)
    finder.addNum(4.0)
    finder.addNum(0.1)
    finder.addNum(10.0)
    finder.addNum(6.3)
    print(finder.findMedian())

    print("Min Heap")
    pq_min = HeapQueue([3, 1, 5, 4, 0, 10, 6])
    for i in range(len(pq_min)):
        print(pq_min.pop())

    print("Max Heap")
    pq_max = HeapQueue([3, 1, 5, 4, 0, 10, 6], heap_type=HeapType.MAX_HEAP)
    for i in range(len(pq_max)):
        print(pq_max.pop())

    pq_str = HeapQueue(['s', 'b', 'abc'])
    pq_str.push('cc')

    for i in range(len(pq_str)):
        print(pq_str.pop())

    pq_str = HeapQueue(['s', 'b', 'abc'], heap_type=HeapType.MAX_HEAP)
    pq_str.push('cc')

    for i in range(len(pq_str)):
        print(pq_str.pop())
