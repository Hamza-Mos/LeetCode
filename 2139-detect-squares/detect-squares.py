class DetectSquares:

    def __init__(self):
        self.points = []
        self.pointsCount = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points.append(tuple(point))
        self.pointsCount[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0

        pointX, pointY = point

        for x, y in self.points:
            # check if the current point is diagonal with input point
            # then check if the rest of the corners of the square (two other points) make a square
            # edge case: a point could be the same as input point (invalid)
            if abs(x - pointX) == abs(y - pointY) and x != pointX and y != pointY:
                res += self.pointsCount[(x, pointY)] * self.pointsCount[(pointX, y)]

        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)