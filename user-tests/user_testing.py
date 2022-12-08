import heapq
from typing import List
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
        self.foo = "bar"
     
    def addNum(self, num: int) -> None:
        return 42

    def findMedian(self) -> float:
        return 42

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
        return 42


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
                heapq.heappush((node.val))
        return head.next


# Our Library Implementation -> TODO
class MergeKListsReimplemented:

    @staticmethod
    def merge(lists):
        return 42




'''
4th: Reimplement Find_K_Closest_Elements (Leetcode - push, pop)
https://leetcode.com/problems/find-k-closest-elements/description/

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

For example, for arr = [1,2,3,4,5], k = 4, x = 3, the result is [1,2,3,4]]
For example, for arr = [1,2,3,4,5], k = 4, x = -1, the result is [1,2,3,4]

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

'''

# Standard Libraries Implementation
class Find_K_Closest_Elements:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        for num in arr:
            heapq.heappush(pq, (abs(num - x), num))
        
        res = []
        while k:
            res.append(heapq.heappop(pq)[1])
            k -= 1
        return sorted(res)


class Find_K_Closest_Elements_Reimplemented:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pass