class Solution:
    def compress(self, chars: List[str]) -> int:
        # length of result array
        # res will always point to position of where the current character should be
        res = 0

        # two pointer approach - left, right
        left = 0

        while left < len(chars):
            right = left
            while right < len(chars) and chars[left] == chars[right]:
                right += 1

            chars[res] = chars[right - 1]
            currGroupLen = right - left

            # update res since at least the currGroupLen will be 1 (character by itself)
            res += 1
            if currGroupLen > 1:
                chars[res : res + len(str(currGroupLen))] = list(str(currGroupLen))
                res += len(str(currGroupLen))

            left += currGroupLen

        return res
        