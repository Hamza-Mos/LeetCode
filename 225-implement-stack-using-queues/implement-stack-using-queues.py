class MyStack:

    def __init__(self):
        # with queues, you can only append to back and pop from front
        self.q = deque()
        

    def push(self, x: int) -> None:
        # let's make sure x is at the front of the queue always!
        self.q.append(x)

        num_elements_in_queue = len(self.q)

        # pop every element that was added before x and append it to the end of the queue
        # leaving x in the front
        for i in range(num_elements_in_queue - 1):
            self.q.append(self.q.popleft())
        

    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()