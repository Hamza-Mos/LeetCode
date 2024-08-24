class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) # maps key -> [timestamp, value]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        vals = self.map[key]

        output = ""
        low, high = 0, len(vals) - 1

        while low <= high:
            mid = low + ((high - low) // 2) # avoids overflow
            time, val = vals[mid]

            if time <= timestamp:
                output = val
                low = mid + 1

            else:
                high = mid - 1

        return output
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)