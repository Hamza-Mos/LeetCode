from collections import deque

class TextEditor:
    def __init__(self):
        self.left = deque()
        self.right = deque()
        
    def addText(self, text: str) -> None:
        # Extend the left deque with the text
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        # Delete up to k characters from the left deque
        tot = 0
        while k and self.left:
            self.left.pop()
            k -= 1
            tot += 1
        return tot
        
    def cursorLeft(self, k: int) -> str:
        # Move the cursor left by transferring characters from left to right
        while k and self.left:
            self.right.appendleft(self.left.pop())
            k -= 1
        return self.getvals()

    def cursorRight(self, k: int) -> str:
        # Move the cursor right by transferring characters from right to left
        while k and self.right:
            self.left.append(self.right.popleft())
            k -= 1
        return self.getvals()
        
    def getvals(self) -> str:
        # Return the last 10 characters from the left deque
        N = len(self.left) 
        return "".join(self.left[i] for i in range(max(N-10, 0), N))
