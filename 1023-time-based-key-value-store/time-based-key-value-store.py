class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        output = ""
        values = self.map[key]

        low, high = 0, len(values) - 1

        while low <= high:
            mid = (low + high) // 2
            time, value = values[mid]

            if time > timestamp:
                high = mid - 1

            else:
                output = value
                low = mid + 1

        return output

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)