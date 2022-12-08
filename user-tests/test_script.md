Thanks for helping us improve our API. We will ask you to complete a single
leetcode question where you will use our new library to complete this question.

This is not a test on you but a test on the API

Follow-up Questions:
- Did you find any problems when working with our library?
  - Specifically, was using the "key" argument helpful?
- Does our library resolve the pain points of heapq
  - *Another phrasing*: Do you believe the code you wrote with our library is more clear/readable compared to the code you would write with the Python heapq library?
- Was there anything you especially liked?
- Is there anything you would change or add on?
------------------------------------------------------------
- Do you think this library should be named HeapQueue or PriorityQueue?
- How is the naming of pop, push, etc? Do you think they should be changed to anything else? Ex. enqueue, dequeue
- Would you find a max size helpful?
- Would you find it helpful to have a __contains__?
- Would `for elem in heap.to_sorted_array()` or `for elem in heap` be more preferable and why?



# Median_finder:
- Did you find any problems when working with our library?
  *Intuitive and comments documentation could be better specifically for key argument. Maybe add "modifies in place"*
- Specifically, was using the "key" argument helpful?
  *Would find this helpful if we were using objects*
- Does our library resolve the pain points of heapq?
  - *Another phrasing*: Do you believe the code you wrote with our library is more clear/readable compared to the code you would write with the Python heapq library?
  *Absolutely*
- Was there anything you especially liked?
  *Didn't have to keep track of negatives for max heap. More clear*
- Is there anything you would change or add on?
------------------------------------------------------------
- Do you think this library should be named HeapQueue or PriorityQueue?          
  *HeapQueue conveys the functionality well*
- How is the naming of pop, push, etc? Do you think they should be changed to anything else? Ex. enqueue, dequeue
  *self explanatory; push could have both functionality of push_all and push. Just modify params* 
- Would you find a max size helpful?
  *potentially helpful for caching. K elems in cache*
- Would you find it helpful to have a __contains__?
  *No, because users generally the ordering of elems in terms of prioirity. In heap is not really used.*
  *Could be helpful for the caching example*
- Would `for elem in heap.to_sorted_array()` or `for elem in heap` be more preferable and why?
  *First one is helpful because it is more clear about time complexitiy and cost*