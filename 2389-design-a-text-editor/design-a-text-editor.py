class TextEditor:

    def __init__(self):
        self.left = deque()
        self.right = deque()
        

    def addText(self, text: str) -> None:
        # add text to left deque
        for char in text:
            self.left.append(char)
        

    def deleteText(self, k: int) -> int:
        num_deleted = 0
        while k and self.left:
            self.left.pop()
            k -= 1
            num_deleted += 1
        
        return num_deleted

    def cursorLeft(self, k: int) -> str:
        # move from left to right
        while k and self.left:
            k -= 1
            char = self.left.pop()
            self.right.appendleft(char)

        starting_index = max(0, len(self.left) - 10)
        remaining_chars = [self.left[index] for index in range(starting_index, len(self.left))]

        return "".join(remaining_chars)
        

    def cursorRight(self, k: int) -> str:
        # move from right to left
        while k and self.right:
            k -= 1
            char = self.right.popleft()
            self.left.append(char)

        starting_index = max(0, len(self.left) - 10)
        remaining_chars = [self.left[index] for index in range(starting_index, len(self.left))]

        return "".join(remaining_chars)
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)