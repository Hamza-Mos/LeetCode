# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

"""

important background for this problem:

Process refers to an instance of a running program. When you execute a program, the operating system 
creates a process for that program. A process has its own memory space, system resources, and execution state.

Threads are the smallest unit of execution within a process. A process can have multiple threads, 
all sharing the same memory space but executing independently. This allows a program to perform 
multiple operations concurrently, making it more efficient, especially in tasks that involve waiting 
(e.g., I/O operations like HTTP requests).

A task is an abstraction for a unit of work. In many programming frameworks, tasks are used to represent 
operations that can be scheduled to run asynchronously or concurrently. A task can be executed by a thread, but 
it doesn’t necessarily map directly to a thread. For example, in an event-driven model like asyncio, many 
tasks might be running on the same thread, switching between tasks as they wait for I/O operations to complete.

ThreadPoolExecutor is a class in Python's concurrent.futures module that allows for managing a 
pool of threads. It is used to efficiently manage multiple threads by reusing a fixed number of threads 
to execute tasks. Instead of creating a new thread for each task (which can be costly in terms of resources), 
ThreadPoolExecutor maintains a pool of threads and assigns tasks to threads in this pool. This reduces the 
overhead associated with thread creation and destruction.

"""

from collections import deque
from concurrent import futures

class Solution:

    def _get_hostname(self, url):
        # Extract the hostname from the URL by splitting the URL by "/" and taking the third element.
        # Example: For "http://example.org/test", it will return "example.org".
        return url.split("/")[2]

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # Extract the hostname from the startUrl
        hostname = self._get_hostname(startUrl)
        
        # A set to keep track of URLs that have already been crawled
        crawled_urls = set([startUrl])

        # Create a ThreadPoolExecutor to manage threads
        with futures.ThreadPoolExecutor() as executor:
            # Initialize a deque (double-ended queue) with a task to fetch URLs from startUrl
            q = deque([executor.submit(htmlParser.getUrls, startUrl)])
            
            while q:
                # Pop a task from the left of the deque
                urls = q.popleft()

                # check if the current task is done or not
                task_is_done = urls.done()
                if not task_is_done:
                    # If not done, re-append the task to the deque
                    q.append(urls)
                    continue

                # Iterate over each URL fetched from the current task
                for url in urls.result():
                    # Check if the URL belongs to the same hostname and hasn't been crawled yet
                    if self._get_hostname(url) == hostname and url not in crawled_urls:
                        # Add the URL to the set of crawled URLs
                        crawled_urls.add(url)
                        
                        # Submit a new task to fetch URLs from the newly found URL and append it to the deque
                        q.append(
                            executor.submit(htmlParser.getUrls, url)
                        )

        # Convert the set of crawled URLs to a list and return it
        return list(crawled_urls)
