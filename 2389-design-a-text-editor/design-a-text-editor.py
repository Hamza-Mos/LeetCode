class TextEditor:
    # use 2 queues
    # one queue for all characters to the left of the cursor
    # other queue for all characters to the right of the cursor

    def __init__(self):
        self.left = deque()
        self.right = deque()
        

    def addText(self, text: str) -> None:
        # text will always be to the left of the current cursor
        for char in text:
            self.left.append(char)
        

    def deleteText(self, k: int) -> int:
        # delete from left of cursor
        num_deleted = 0
        while num_deleted < k and self.left:
            self.left.pop() # append from end of left queue
            num_deleted += 1

        return num_deleted
        

    def cursorLeft(self, k: int) -> str:
        # move characters from left queue to right queue
        while k and self.left:
            char = self.left.pop() # pop from end of left queue
            self.right.appendleft(char) # append to front of right queue
            k -= 1

        # return min(10, len) characters in the left queue
        left_index = len(self.left) - min(10, len(self.left))

        vals = [self.left[i] for i in range(left_index, len(self.left))]

        return "".join(vals)
        

    def cursorRight(self, k: int) -> str:
        # move characters from right queue to left queue
        while k and self.right:
            char = self.right.popleft() # pop from front of right queue
            self.left.append(char) # append to end of left queue
            k -= 1

        # return min(10, len) characters in the left queue
        left_index = len(self.left) - min(10, len(self.left))

        vals = [self.left[i] for i in range(left_index, len(self.left))]

        return "".join(vals)
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)