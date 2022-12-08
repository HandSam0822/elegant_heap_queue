'''
User: Lulu Lin (yijunglin)
Date: 12/6/22
'''
import heapq
from source.heap_queue import HeapQueue, HeapType

'''
User-Testing Follow-up Questions:

- Did you find any problems when working with our library?
    Did not understand the setting of max_size and wondering if this setting will be used much.
    I believe this would add constraints and be more inconvenient when users initialize with this parameter.

  - Specifically, was using the "key" argument helpful?
    Yes, the design is align with official Python sort nethod, so I feel intuitive to pass in lambda function.
    However, it would be better if the documention provide some examples.

- Does our library resolve the pain points of heapq?
    Yes, personally do not appreciate the heapq library for users to pass negative value to achieve max heap cause it is really hard to understand during code review.
    Thus, I like the idea of passing the argument to distinguish minheap and maxheap. 
    

- Was there anything you especially liked?
    The naming of functions and parameters in your library is easy to understand and more readable.
    In the current python library, I actually think they included many redundant functions to make programming simple but instead of making it need more explanations.
    Take "push_pop" for example, when I read this function in code that I haven't seen before, I would need to google the documentation to understand its usage and purpose.
    Besides, I really like your library since we do not have to add "heapq" in front of every operation when using current Python library.

- Is there anything you would change or add on?
    There's only one thing I would like to recommend. If we could initialize the max heap as `myheap  = PriorityQueue(max=true)`
    it would be more convenient for users since not all users would appreciate memorizing the name of Heap type Enum. (despite that it provides better readibility)

    In the beginning, I do not understand why there should be "push_all" function if you can just pass the list as "items" when initialize the heap.
    But after understanding the purpose of this function which is to push elements on an existed heap, I could see its value now.
    

------------------------------------------------------------
- Do you think this library should be named HeapQueue or PriorityQueue?
    Personally prefer HeapQueue since the formal data structure is called "heap", I believe.

- How is the naming of pop, push, etc? Do you think they should be changed to anything else? Ex. enqueue, dequeue
    I personally prefer "push" and "pop" and believe this is more intuitive when programming.

- Would you find a max size helpful?
    Based on my past experience, I do not think the setting would be much helpful. 
    Programmers can achieve this by customized constrain in their code based on their needs. 
    I believe this way is simpler.

- Would you find it helpful to have a __contains__?
    Though I haven't find much scenario that needs to check whether an element is in the PriorityQueue, I do think that providing
    it makes the API more resourceful. 
    

- Would `for elem in heap.to_sorted_array()` or `for elem in heap` be more preferable and why?
    Although I think the first one fits more with the Python convention coding style, I personally prefer the second one. 
    I believe this way is more clear. When users try to iterate a heap, we are expecting it returns as a sorted array.
    Thus if the default library is implemented like this, one can reduce the chance to get errors.
'''