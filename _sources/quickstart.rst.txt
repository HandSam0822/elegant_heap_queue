Quickstart
==========

The Elegant Heap Queue package contains resourceful API for Python developer better using Priority Queue to achieve their goal.
Considering that there're lots of inconvenience when using existing Python PQ library such as `heapq`_ and `queue.PriorityQueue`_


.. _heapq: https://docs.python.org/3/library/heapq.html

.. _queue.PriorityQueue: https://docs.python.org/3/library/queue.html

Thee detailed can be found in :doc:`apidocs`.


Usage
~~~~~

::

    pip install elegant-heap-queue

It's also possible to use the library files uploaded to the `PyPI`_  website directly in your projects.

.. _PyPI: https://pypi.org/project/elegant-heap-queue/



Getting Started with Elegant Heap Queue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Constructor Arguments
The most basic way to instantiate a TODOQueue, heap = HeapQueue(). However, there are many different arguments that help elevate the usefulness of this library:


.. list-table:: Constructor Arguments
   :widths: 50 50 50
   :header-rows: 1

   * - Argument Name
     - Description
     - Example
   * - items
     - Iterable of initial items to push to the TODOQueue
     - ``heap = HeapQueue(items=[1, 2, 3])``
   * - heap_type
     - Defines the ordering of the items within the PriorityQueue. Default value MIN_HEAP
     - ``heap = HeapQueue(HeapQueue(heap_type=HeapType.MAX_HEAP))``

   * - key
     - Key function to define the value which an item's "priority" should be generated from. Generally, used when the HeapQueue's type is a custom class
     - ``heap = HeapQueue(key=lambda x: x.val)``


.. list-table:: Core Functions
   :widths: 50 50 50
   :header-rows: 1

   * - Function
     - Description
     - Example
   * - ``peek``
     - Returns (but does not remove) the highest priority item
     - ``heap.peek()``
   * - ``push``
     - Pushes the item onto the TODOQueue, while maintaining heap invariant	
     - ``heap.push(1)``
   * - ``push_all``	
     - Takes an iterable which will add all elements to heap	
     - ``heap.push([1, 2, 3])``
   * - ``pop`` 	
     - Returns and removes the highest priority item	
     - ``heap.pop()``
   * - ``pop_k``	
     - Returns and removes the k highest priority items	
     - ``heap.pop_k(2)``
   * - ``as_sorted_list``  
     - Returns all items in the TODOQueue as a sorted list based on priority	
     - ``for item in heap.as_sorted_list(): ...``