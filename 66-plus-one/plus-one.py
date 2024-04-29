class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry

            carry = digits[i] // 10
            digits[i] = digits[i] % 10

        if carry:
            return [carry] + digits

        return digits