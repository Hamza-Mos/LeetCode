class Solution:
    def checkValidString(self, s: str) -> bool:
        # leftMin -> the min number of open parens we can have (decrement with closed parens)
        # leftMax -> the max number of open parens we can have (decrement with closed parens)
        # both of these depend on the number of wildcards we can have
        leftMin = leftMax = 0

        for char in s:
            if char == "(":
                leftMin += 1
                leftMax += 1

            elif char == ")":
                leftMin -= 1
                leftMax -= 1

            # wildcard
            else:
                leftMin -= 1
                leftMax += 1

            # if leftMax ever becomes negative then it is not a valid string
            if leftMax < 0:
                return False

            # if leftMin ever becomes negative then we should reset it to 0
            # ex: (*)( can never be valid however without this condition, the function would return True when it shouldnt
            if leftMin < 0:
                leftMin = 0

        return leftMin <= 0 <= leftMax
        