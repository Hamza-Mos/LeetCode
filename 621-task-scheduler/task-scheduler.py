class Solution:
    def greadySolution1(self, tasks, n):
        # create a frequency array
        freq = [0] * 26

        for c in tasks:
            freq[ord(c) - ord('A')] += 1

        freq.sort() # sorting the array is an O(1) operation because there are a max of 26 characters to sort

        maxFreq = freq[-1]

        # total number of possible idleSlots (we subtract 1 from maxFreq because no idle
        # slots for last task
        maxFreq -= 1
        idleSlots = maxFreq * n

        # loop over each element except last one (already processed for maxFreq)
        # subtract their occurrences from idleSlots
        for i in range(0, 25):
            # if there is another element in the array that occurs same number of times as max freq task
            # then we would also need to subtract 1 from it (since we do not care about last occurrence
            # of the max freq tasks)
            idleSlots -= min(freq[i], maxFreq)

        idleSlots = max(0, idleSlots) # idle slots cannot be negative

        # the total number of time slots taken to process all tasks will be all tasks + number of idle slots taken
        return len(tasks) + idleSlots

    def greedySolution2(self, tasks, n):
        freq = collections.Counter(tasks)

        # max freq task value
        maxFreq = max(freq.values())

        # number of time slots at the end for each task that has the same freq as maxFreq
        endSlots = sum(map(lambda count: count == maxFreq, freq.values()))  

        # the max number of slots for the maxFreq tasks are (n + 1) * (maxFreq - 1) which is 1 for processing
        # the task itself and n for the idle time between each process + 1 for each process that has a count
        # of maxFreq which would occur at the end (no idle time included for last occurrence)
        totalSlots = (n + 1) * (maxFreq - 1) + endSlots

        return max(totalSlots, len(tasks))
    
    def heapSolution(self, tasks, n):
        freq = collections.Counter(tasks)

        # build max heap
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        # queue for tasks
        q = deque()

        time = 0

        while maxHeap or q:
            time += 1

            # if there are no more tasks left to process (in maxHeap) then jump to time to process next task
            # this would skip idle time
            if not maxHeap:
                time = q[0][1]

            # process tasks in max heap
            else:
                count = 1 + heapq.heappop(maxHeap)

                # if there are still more tasks of this type to process then add them to queue (with time
                # of when this task will be available again)
                if count:
                    q.append((count, time + n))

            # we have reached time to add task back to max heap
            if q and q[0][1] == time:
                count, time = q.popleft()
                heapq.heappush(maxHeap, count)

        return time


    def leastInterval(self, tasks: List[str], n: int) -> int:
        return self.greedySolution2(tasks, n)