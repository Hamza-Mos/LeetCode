class TimeMap:

    def __init__(self):
        self.cache = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        value = ""

        # do binary search and find the nearest timestamp
        low, high = 0, len(self.cache[key]) - 1

        while low <= high:
            mid = (low + high) // 2

            val, time = self.cache[key][mid]

            if time <= timestamp:
                value = val
                low = mid + 1

            else:
                high = mid - 1

        return value
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)