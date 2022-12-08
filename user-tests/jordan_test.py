'''
User: Jordan Gilbert (jtgilber)
Date: 12/3/22
'''

import heapq
from source.heap_queue import HeapQueue, HeapType

'''
1st: Reimplement Median Finder (Leetcode - peek, pop, push, min, max)

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''

# Standard Libraries Implementation
class MedianFinderStandard:
    
    def __init__(self):
        # smaller half of data. maxHeap[0] stores the biggest data in smaller half
        self.maxHeap = []
        # bigger half of data. minHeap[0] stores the smallest data in bigger half 
        self.minHeap = []
      
    def addNum(self, num: int) -> None:
       if len(self.maxHeap) > len(self.minHeap):
           x = heapq.heappushpop(self.maxHeap, -num)
           heapq.heappush(self.minHeap, -x)
       else:
           y = heapq.heappushpop(self.minHeap, num)
           heapq.heappush(self.maxHeap, -y)

    def findMedian(self) -> float:
       # if number of element is odd, median is biggest element in maxHeap
       if (len(self.maxHeap) + len(self.minHeap)) % 2 != 0:
           return -(self.maxHeap[0])
       # if number of element is even, median is the mean of greatest element in maxHeap and smallest element in minHeap
       return (-self.maxHeap[0] + self.minHeap[0]) / 2


class MedianFinderReimplemented:
    
    def __init__(self):
        self.maxHeap = HeapQueue(heap_type=HeapType.MAX_HEAP)
        self.minHeap = HeapQueue(heap_type=HeapType.MIN_HEAP)
     
    def addNum(self, num: int) -> None:
        #if self.maxHeap._max_size > self.minHeap._max_size:
        if len(self.maxHeap.items) > len(self.minHeap.items):
            self.maxHeap.push(num)
            x = self.maxHeap.pop()
            self.minHeap.push(x)
        else:
            self.minHeap.push(num)
            y = self.minHeap.pop()
            self.maxHeap.push(y)

    def findMedian(self) -> float:
        #if self.maxHeap._max_size + self.minHeap._max_size % 2 != 0:
        if (len(self.maxHeap.items) + len(self.minHeap.items)) % 2 != 0:
            return self.maxHeap.pop()
        return (self.maxHeap.pop() + self.minHeap.pop()) / 2

'''
2nd: Reimplement Kth largest Elements (Leetcode - push, pop, peek, pop_k, len)

Given a list of integers 'nums' and integer 'k', return the kth largest elements in the array.

Note that it is the kth largest elements in the sorted order, not the kth distinct element; 
also assume len(nums) >= k.
'''

# Standard Libraries Implementation
class KthLargestElementsStandard:

    @staticmethod
    def find(nums: list[int], k: int) -> int:
        minHeap = []
        for i in range(0, len(nums)):
            # only if heap has size k see if elem needs to be removed
            if len(minHeap) == k:
                x = minHeap[0]
                if x < nums[i]:
                    heapq.heappop(minHeap)
                    heapq.heappush(x)
            else:
                heapq.heappush(minHeap, nums[i])

        return heapq.nlargest(k, minHeap)

# Our Library Implementation -> TODO
class KthLargestElementsReimplemented:

    @staticmethod
    def find(nums: list[int], k: int):
        maxHeap = HeapQueue(heap_type=HeapType.MAX_HEAP)
        maxHeap.push_all(nums)
        return maxHeap.pop_k(k)


'''
3rd: Reimplement merge K sorted lists (pop, push, key fn, push_all/init_list)

https://leetcode.com/problems/merge-k-sorted-lists/solution/

You are given an array of 'K' linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Assume no null values in the input 'lists'
'''

# ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Standard Libraries Implementation
class MergeKListsStandard:

    @staticmethod
    def merge(lists):
        head = point = ListNode(0)
        minHeap = []
        for node in lists: # alternatively could map and use .heapify(...)
            heapq.heappush((node.val, node))
        while len(minHeap) > 0: # or while not len(minHeap)
            (val, node) = heapq.heappop(minHeap)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush((node.val, node))
        return head.next


# Our Library Implementation -> TODO
class MergeKListsReimplemented:

    @staticmethod
    def merge(lists):
        head = point = ListNode(0)
        minHeap = HeapQueue(
            heap_type=HeapType.MAX_HEAP,
            key=lambda n: n.val
        )
        minHeap.push_all(lists)
        while len(minHeap) > 0:
            node = minHeap.pop()
            point.next = ListNode(node.val)
            point = point.next
            if node.next != None:
                minHeap.push(node.next)
        return head.next

'''
User-Testing Follow-up Questions:

- Did you find any problems when working with our library?
    The parameter max_size was unclear from its description; potentially unclear for getting size of heap or max_size.

  - Specifically, was using the "key" argument helpful?
        It was helpful but confusing at first glance, might need to be better documented and explained. However, never used Python lambda's
        before so might influence answer somewhat.

- Does our library resolve the pain points of heapq?
  - *Another phrasing*: Do you believe the code you wrote with our library is more clear/readable compared to the code you would write with the Python heapq library?
        Definitely as demonstrated by first question which was very unintuitive before. Liked that the HeapQueue class allowed better encapsulation of the full logic
        required for a PQ in Python. Surprised that no better standard libraries existed.

- Was there anything you especially liked?
    push_all and pop_k were nice conveniences, no need to do negations because of changeable order, 

- Is there anything you would change or add on?
    max_size and push_all could be better explained for what they can take in. Potentially ability to make PQ "unique" and guarantee all elems
    are unique (said might be uses in stats/ML for this).

------------------------------------------------------------
- Do you think this library should be named HeapQueue or PriorityQueue?
    PriorityQueue -> Its in the name what it does/how it works.

- How is the naming of pop, push, etc? Do you think they should be changed to anything else? Ex. enqueue, dequeue
    push and pop better. Said to consider "add" over "push" because push makes you think it will be in a specific spot in the data structure ("pushed on"), whereas "add" is like "I added it in and its somewhere in the
    Queue based on the Priority logic". Said "pop" seems right, however, (pop it from the top).

- Would you find a max size helpful?
    it could be depending on situation, but seems very narrow. maybe a good feature to have.

- Would you find it helpful to have a __contains__?
    Seems useful, there are times in general where its useful to check if its "in" the data structure even if PQ doesn't do often.

- Would `for elem in heap.to_sorted_array()` or `for elem in heap` be more preferable and why?
    Former seems better, tells cost + how the iteration is occurring.
'''