class TwoSum:

    def __init__(self):
        self.count = {}
        

    def add(self, number: int) -> None:
        self.count[number] = self.count.get(number, 0) + 1
        

    def find(self, value: int) -> bool:
        for num in self.count:
            if num == value - num:
                if self.count[num] > 1:
                    return True
            elif value - num in self.count:
                return True

        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)