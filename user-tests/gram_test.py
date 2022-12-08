'''
User: Gram Liu (gdl2)
Date: 12/5/22
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
        self.maxHeap = HeapQueue(heap_type = HeapType.MAX_HEAP)
        self.minHeap = HeapQueue(heap_type = HeapType.MIN_HEAP)
     
    def addNum(self, num: int) -> None:
        if len(self.maxHeap) > len(self.minHeap):
            self.maxHeap.push(num)
            self.minHeap.push(self.maxHeap.pop())
        else:
            self.minHeap.push(num)
            self.maxHeap.push(self.minHeap.pop())

    def findMedian(self) -> float:
        if (len(self.maxHeap) + len(self.minHeap)) & 1 == 0:
            # Even; get mean of middle vals
            left = self.minHeap.peek()
            right = self.maxHeap.peek()
            return (left + right) / 2

        return self.maxHeap.peek()

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
        max_heap = HeapQueue(nums, heap_type = HeapType.MAX_HEAP)
        return max_heap.pop_k(k)


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
    def merge(lists: list[ListNode]):
        minHeap = HeapQueue(heap_type = HeapType.MIN_HEAP, key=lambda node: node.val)
        for linked_list in lists:
            node = linked_list
            while node != None:
                minHeap.push(node)
                node = node.next
        
        new_head = minHeap.pop()
        node = new_head
        while len(minHeap) > 0:
            next = minHeap.pop()
            node.next = ListNode(next.val, next.next)
            node = next
        node.next = None

        return new_head


'''
User-Testing Follow-up Questions:

- Did you find any problems when working with our library?
    No
    

  - Specifically, was using the "key" argument helpful?
  yes
        

- Does our library resolve the pain points of heapq?
  - *Another phrasing*: Do you believe the code you wrote with our library is more clear/readable compared to the code you would write with the Python heapq library?
    Yes

- Was there anything you especially liked?
   I really liked how much more elegant it was to make max heaps as opposed to the negation approach required by heapq

- Is there anything you would change or add on?
   Nothing really other than that I recommend you publish this bc it's really helpful and well-designed. 10/10 would use again

------------------------------------------------------------
- Do you think this library should be named HeapQueue or PriorityQueue?
    I think HeapQueue makes sense because most Python users are familiar with heapq

- How is the naming of pop, push, etc? Do you think they should be changed to anything else? Ex. enqueue, dequeue
    pop/push makes sense since they're much more concise

- Would you find a max size helpful?
    not really

- Would you find it helpful to have a __contains__?
    no

- Would `for elem in heap.to_sorted_array()` or `for elem in heap` be more preferable and why?
    to_sorted_array because it more clearly emphasizes the fact that you're performing some computation
    since you have to call a function first as opposed to a `for-in` loop where most users just assume
    the iterator can run in constant time
'''