class TextEditor:

    def __init__(self):
        self.text = []
        self.cursor = 0

    def addText(self, text: str) -> None:
        # Insert text at the cursor position
        self.text[self.cursor:self.cursor] = list(text)
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        # Calculate the actual number of characters to delete
        delete_count = min(k, self.cursor)
        self.text[self.cursor - delete_count:self.cursor] = []
        self.cursor -= delete_count
        return delete_count

    def cursorLeft(self, k: int) -> str:
        # Move the cursor to the left by k positions
        self.cursor = max(0, self.cursor - k)
        start = max(0, self.cursor - 10)
        return ''.join(self.text[start:self.cursor])

    def cursorRight(self, k: int) -> str:
        # Move the cursor to the right by k positions
        self.cursor = min(len(self.text), self.cursor + k)
        start = max(0, self.cursor - 10)
        return ''.join(self.text[start:self.cursor])

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)

# Example usage:
# textEditor = TextEditor()
# textEditor.addText("leetcode")     # The current text is "leetcode|".
# print(textEditor.deleteText(4))    # return 4, The current text is "leet|".
# textEditor.addText("practice")     # The current text is "leetpractice|".
# print(textEditor.cursorRight(3))   # return "etpractice"
# print(textEditor.cursorLeft(8))    # return "leet"
# print(textEditor.deleteText(10))   # return 4, The current text is "|practice".
# print(textEditor.cursorLeft(2))    # return ""
# print(textEditor.cursorRight(6))   # return "practi"
