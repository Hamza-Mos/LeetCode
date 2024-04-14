class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionAndSpeed = [[pos, sp] for pos, sp in zip(position, speed)]

        # we want position to be sorted in reverse (we want to process)
        positionAndSpeed.sort(reverse=True)
        
        numFleets = 0
        prevTime = 0
        fleets = 0

        for pos, sp in positionAndSpeed:
            # calculate time to reach target
            time = (target - pos) / sp

            if time > prevTime:
                fleets += 1
                prevTime = time

        return fleets