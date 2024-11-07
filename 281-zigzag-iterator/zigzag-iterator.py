class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.p1 = self.p2 = 0
        self.move_v1 = True
        

    def next(self) -> int:
        found_num = False
        num = 0
        if self.move_v1 and self.p1 < len(self.v1):
            self.p1 += 1
            num = self.v1[self.p1 - 1]
            found_num = True

        elif self.p2 < len(self.v2):
            self.p2 += 1
            num = self.v2[self.p2 - 1]
            found_num = True

        self.move_v1 = not self.move_v1
        if not found_num:
            return self.next()
        return num
            
        

    def hasNext(self) -> bool:
        return self.p1 < len(self.v1) or self.p2 < len(self.v2)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())