class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # reverse sorted positions and speeds
        posAndSpeed = sorted(zip(position, speed), reverse=True)

        time = float('-inf')
        fleets = 0

        for pos, sp in posAndSpeed:
            newTime = (target - pos) / sp
            if newTime > time:
                fleets += 1
                time = newTime

        return fleets
        