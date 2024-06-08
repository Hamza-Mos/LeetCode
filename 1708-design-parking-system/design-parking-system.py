class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]
        

    def addCar(self, carType: int) -> bool:
        index = carType - 1

        if self.slots[index] > 0:
            self.slots[index] -= 1
            return True

        else:
            return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)