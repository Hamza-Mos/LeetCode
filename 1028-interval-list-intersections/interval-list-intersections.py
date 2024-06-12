class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        p1 = p2 = 0

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            # overlap
            if not (end1 < start2 or end2 < start1):
                intersections.append([max(start1, start2), min(end1, end2)])

            if end1 < end2:
                p1 += 1

            else:
                p2 += 1

        return intersections