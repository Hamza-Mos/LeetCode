class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[0, 0]] for i in range(length)]
        self.snapId = 0
        

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snapId, val])
        

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1
        

    # we want to return the latest value for the current index before snap_id + 1
    def get(self, index: int, snap_id: int) -> int:
        # this will return the rightmost insertion index in the given version snap_index
        snapIndex = bisect.bisect_right(self.array[index], [snap_id, float('inf')])
        return self.array[index][snapIndex - 1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)