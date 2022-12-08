# Code in the Wild 

## Example 1 (Dijkstras + Huffman)
- [Dijkstras Java](https://github.com/mburst/dijkstras-algorithm/blob/master/Dijkstras.java) => PQ "Vertex" class type implements a comparable instead of creating a tuple as seen in heapq/Python; Overrides .compareTo(...) function. 
- [Dijkstras Python](https://github.com/mburst/dijkstras-algorithm/blob/master/dijkstras.py) => Line 46: Python heap needs to constantly reorder elems when an elem is changed. Java implementation does not do this but removes the node from PQ, changes val, then adds node back into PQ. Not sure what decisions to make off this.
- [Huffman Java](https://github.com/nayuki/Reference-Huffman-coding/blob/bc286358d24b81cd06287b3b062da54388e2ee67/java/src/FrequencyTable.java) => PQ "node" class type also implements a comparable interface to create priority for PQ.
- [Dijkstras C++](https://github.com/josefgraus/self_similarity/blob/c032daa3009f60fdc8a52c437a07c6e3ba2efe4b/src/algorithms/shortest_path.cpp) => Note verbose .top(...), .pop(...) code pattern for simle 'pop' actions. 

## Example 2 (Popping Multiple)
- [Using heapq nlargest/nsmallest](https://github.com/colinaardsma/gsa/blob/fe738bbda48bdbda1b06c19cf3ec1c1b96a3fac9/projections/helpers/player_creator.py) => Many uses of heapq's "nlargest/nsmallest" functions, it is a partial convinence for loops (code would be MUCH more verbose w/ out) but likely need to keep the utility in our library.
- [Another heapq nlargest](https://github.com/joint-em/FirmCore/blob/2e44d1f3e73822cf02f59b4f23d76e2c5187b041/Code/FirmCore_Decompositions.py) => heapq "nlargest" being used to essentially _pop\_n_ from the PQ based on priority then grab the last. Again, here used as a partial convienence for larger loops.
- [KLarestElements Java](https://github.com/sumitsrv121/DSA_Practice/blob/4d19dc3ecf26759e91339d1e6b4f06daa18bc832/src/main/java/com/sumit/srv/heap/KLargestElementsOfAnArray.java) => Simple use-case, but shows too that sometimes you just want to _pop\_n_ number of elements from list instead of having to loop. Java devs do the equivalent functionality as nlargest/nsmallest but need to incorporate a loop and increase verbosity. However, also possible that it is a very narrow use-case for algos specifically... 

## Example 3 (PQ Traversal)
- [PQ Traversal Python](https://github.com/Leesungsup/algo-test/blob/582d62666e1337519c3d80c6faf7b19c9e20b4cc/heap.py) => Code uses a while loop to iterate through elements keeping the PQ order that matters, might be nice to be able to reduce code for this. Iterator works well with for-each and other built in Python functions like enumerate
- [PQ Traversal Java](https://github.com/LayneFongX/Hodgepodge/blob/9229c4b8e9b8800b936adbebc52dc5be652cff1f/queue/src/main/java/com/laynefongx/hodgepodge/service/impl/PriorityQueueService.java) => Java code also access an iterator to try and traverse (doesn't do it right) the entire contents of the built PQ. Seems PQs are used often for testing purposes and that they are traversed for test cases often too. 
- [HDFS Balance Plan Java](https://github.com/ryneli/RsyncCopy/blob/0939fb6d9deac89187d196d31df9bced758661fb/hdfs/org/apache/hadoop/hdfs/server/balancer/BalancePlan.java) => Several for-each loops over PQ using iterator pattern (line 242 ex.); Not entirely clear from code, however, how for-each traversal works or performance implications
- Extra Notes: If we added this feature, it needs to be very clear how for-each traversal would work, performance implications, and memory ownership.

## Example 4 ("Heapify" / Adding Multiple)
- [Heap Sort C](https://github.com/Bossmo02/SortingAlgorithms/blob/8ca981acb76c2f52fa1b2bdc2121d303bb932484/HeapSort.h) => C doesn't translate as well, but its clear from HeapSort approach that there should be a "heapify" ability for constructor that takes in a pre-existing collection to create initial heap (avoid redundant loops to push element). Also potentially as a follow up "add/push_all(...)" convienence method for a very similar reason as just described...
- [KLargestElems Java](https://github.com/an-infinity/Algorithms/blob/76ee8472890b041ccc88abf83926ae1d4730b03e/running_median.py) => Like above code ^^^ there really needs to be a way to init with a collection or add/push_all(...) elements onto the PQ to avoid unnecessary verbosity. Also , raises the question of _what should string representation of our PQ be_?
- [Giraph-core Partition Balancer Java](https://github.com/zjianliu/giraph-1.2.0/blob/a822fc3beec68888e228af93ea3b141143c147fa/giraph-core/src/main/java/org/apache/giraph/partition/PartitionBalancer.java) => Demonstrates init with a preexisting collection (Line 292). 

## Example 5 (Miscellanous)
https://github.com/an-infinity/Algorithms/blob/76ee8472890b041ccc88abf83926ae1d4730b03e/running_median.py
- Notes:
  - Median Finder simple use-case demonstrates odd interface and client code using heapq as it is right now
  - One of the examples we can test our implementation with

## Example 6 (Complex Priority)
- [Launch Queue Typescript](https://github.com/noslate-project/noslated/blob/b6bae04799b498c4a16cb3641680e9c4af86f6d0/src/control_plane/priority_launch_queue.ts) => Typescript code shows that there are often more complex priorities that clients want to use for PQ (especially on non-trivial things), achieved using a comparater. This would be much uglier and less intutitive with a Python std lib. Also seems like people are used to .isEmpty() method...
- Other examples below...

# Example 7 (Real PQ Balancer Applications)
- [Priority Balancer Java](https://github.com/jma19/LoadBalancer/blob/899e72a74e37a8e41bb30f150c6942ad6954ce0e/LoadBalancer/src/main/java/com/uci/routing/PriorityBalancer.java) => 
- [Session Loadbalancer Java](https://github.com/Kixeye/janus/blob/a8a8fc5e6e1306239d42b92fdc34fc889cba19c2/janus-core/src/main/java/com/kixeye/janus/loadbalancer/SessionLoadBalancer.java) => Using init_size argument for constructor. Uses a similar tuple heapq method for elements but its a class with a custom comparator. 
- [Hadoop Greedy Balancer Java](https://github.com/techwhizbang/ozone/blob/d6e0e4747f09ce5c04bcd2ac42cf9ce3e73198db/hadoop-hdds/server-scm/src/main/java/org/apache/hadoop/hdds/scm/container/balancer/FindSourceGreedy.java) => Complex priority comparator lambda used. Java .addAll(...) function is used when possible to write simpler code. Java .clear(...) is used to reset PQ, _question of if we should have this use case_? (Basically convience for loop to pop)
- [Websockets Endpoint Performance Table Java](https://github.com/Luc14860/jwebsocket/blob/b37f087a80e523008c184bfaf761243db3b3f011/branches/jWebSocket-1.0/jWebSocketPlugIns/jWebSocketLoadBalancerPlugIn/src/main/java/org/jwebsocket/plugins/loadbalancer/EndPointsPerformanceTable.java) => Like above ^^^ has what should be an easy application of an .addAll() function. 
- [Pinterest Parition Balance Strategy Java](https://github.com/pinterest/memq/blob/9a56133c0f4d667bd723852ee3469e2fb181c2cf/memq/src/main/java/com/pinterest/memq/core/clustering/PartitionBalanceStrategy.java) => Again, demonstrates need for complex and customizable PQ comparator (Line 120). .addAll(...) utilized when possible (would look much grosser without), .clear(...) utilized. Both size and .isEmpty() function are utilized for different use-cases. 
- [HDFS Balance Plan Java](https://github.com/ryneli/RsyncCopy/blob/0939fb6d9deac89187d196d31df9bced758661fb/hdfs/org/apache/hadoop/hdfs/server/balancer/BalancePlan.java) => Demonstrates .addAll(...) is a separate use case depending on the other actions necessary when traversing the collection you wish to insert elems from. Also, shows several for-each loops over PQ using iterator pattern (line 242 ex.)
- [Scheduler Python](https://github.com/marmiksp/Distributed_MLOps_Application_Platform/blob/30b562599f258cef0fa0cab163fb43228be74776/Scheduler/Scheduler.py) => Demonstrates just how confusing Python std libraries can be for PQs with tuple inputs and opaque slicing... should be much better encapsulated.
- [YahooProtocol Python](https://github.com/ifwe/digsby/blob/f5fe00244744aa131e07f09348d10563f3d8fa99/digsby/src/yahoo/YahooProtocol.py) => Several points where there should have been a add/push_all utility to simplify code with a map (Line 291, 299, etc.) Uses really chunky __cmp__ magic method to hack heapq.
- [Scheduler C++](https://github.com/tbarbette/fastclick/blob/f99c521dd46341394a1343dccc043f3625360435/vendor/nicscheduler/methods/solver.hh) => empty utility function still used in C++ client code often. Several spots where addAll would have been applicable (line 108). Gross top()/pop() function sequence.
- Extra Notes => isEmpty() seems HEAVILY utilized throughout all the different platforms and as a concept for PQs (even with size also being there, seem to be different use-cases)..., idea of a .clear(...) utility function is also intriguing, C++ has a top() followed by pop() to perform basic pop from PQ, Java seemed to fix this weird pattern with single poll() and should be kept.

## Other Implementations
- https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/PriorityQueue.html
- https://en.cppreference.com/w/cpp/container/priority_queue

## TODO
- Use-case for .to_inorder_array(...) func
- Use-case for max_size constant
- Can init_size constant be a thing for Python? Heavily used in Java.
