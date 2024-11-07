class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.outer = 0 # points to the row in the 2D vector
        self.inner = 0 # points to the column in the 2D 
        self.move_pointer()

    def move_pointer(self):
        while self.outer < len(self.vec) and self.inner >= len(self.vec[self.outer]):
            self.inner = 0
            self.outer += 1
        

    def next(self) -> int:
        num = self.vec[self.outer][self.inner]
        self.inner += 1
        self.move_pointer()

        return num

    def hasNext(self) -> bool:
        return self.outer < len(self.vec)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()