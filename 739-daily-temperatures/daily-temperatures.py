class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        # monotonically decreasing stack

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prevTemp, index = stack.pop()
                res[index] = i - index

            stack.append([temp, i])

        return res