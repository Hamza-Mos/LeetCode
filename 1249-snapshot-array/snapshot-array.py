class SnapshotArray:

    def __init__(self, length: int):
        # 2D array
        # basically an array of given length
        # each element contains an array of tuples (snapId, value)

        self.vals = [ [[0, 0]] for row in range(length) ]
        self.snapId = 0

        

    def set(self, index: int, val: int) -> None:
        latestSnapId = self.vals[index][-1][0]

        if latestSnapId == self.snapId:
            # sets latest snap value to val
            self.vals[index][-1][1] = val

        else:
            # add tuple because latest value has outdated snap id
            self.vals[index].append([self.snapId, val])
        

    def snap(self) -> int:
        self.snapId += 1

        return self.snapId - 1
        

    def get(self, index: int, snap_id: int) -> int:
        # look for value with biggest snapId that is <= passed snap_id
        # binary search

        vals = self.vals[index]

        low, high = 0, len(vals) - 1
        output = -1

        index = bisect.bisect_left(vals, [snap_id, float('inf')])

        return vals[index - 1][1]

        while low <= high:
            mid = (low + high) // 2

            snapId, val = vals[mid]

            if snapId <= snap_id:
                output = val
                low = mid + 1

            else:
                high = mid - 1

        return output
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)