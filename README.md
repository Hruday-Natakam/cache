# cache
We will use Python to simulate a cache with two management techniques.

Background:

In computers, memory is located in different parts of the computer; memory on disk is far away from the CPU and takes a long time to access, but offers a large amount of storage; cache memory is close to the CPU, so it is faster to access, but does not offer a lot of storage space.

It is therefore wise to use the cache memory in a smart way, so that pages of memory that are more likely to be accessed are already in the cache. This means that there are fewer accesses to disk memory, and the memory transaction is ultimately quicker.

In this assignment, you will use Python to simulate a cache with two management techniques, which are explained below. 

The cache memory operates in the following manner:

Pages from memory are requested. When a page from memory is requested, the cache memory is searched for that page. 

If the page is found in the cache memory, then this is called a "hit".
If the page is not found in the cache memory, then this is called a "miss".  When a miss happens, the page must be retrieved from the main memory (the disk memory) and must be placed in the cache memory. If the cache memory is not full, then the page is simply added to the cache memory. If the cache memory is full, then one of the pages that is in the cache memory will have to be replaced. In this case, we say that a new page is added to the cache memory, and the old page is evicted. 
There are multiple ways in which we can choose which page to evict. Two of those are presented below, the "First in First Out (FIFO)" algorithm, and the "Least Frequently Used (LFU)" algorithm.

First in First Out (FIFO)
In a First in First Out (FIFO) cache memory, the page that is evicted is the one that has the longest time since it was added.

Least Frequently Used (LFU)
In a Least Frequently Used (LFU) cache memory, the page that is evicted is the page that has had the fewest requests so far. In case of two pages having the same amount of requests, the lowest numbered page should be evicted. The number of requests that a page has had is maintained throughout the parsing of the whole set of requests, and it is not "forgotten" once a page has been removed from the cache memory.

 

Specifics:

In this exercise, we will assume that

every page is represented by a positive integer.
the capacity of the cache memory is 8 pages. 
In particular, a request for a page will be indicated by a number, e.g., the number 3 means that we request page 3. If the requested page is in the cache memory, then this will be a hit. If the requested page is not in the cache memory, then this will be a miss. In this latter case, the page has to be retrieved from the main memory and placed into the cache memory. If the cache memory is not full (i.e., it has fewer than 8 pages already in it), then we can simply add the requested page to the cache memory. If the cache memory is full (meaning that it has exactly 8 pages in in), then we have to evict one page already in the cache memory, in order to bring the newly requested page in. Which page to evict is decided based on one of the two algorithms above, FIFO or LFU.
