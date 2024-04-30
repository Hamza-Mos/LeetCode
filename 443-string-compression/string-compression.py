class Solution:
    def compress(self, chars: List[str]) -> int:
        # length of result array
        # res will always point to position of where the current character should be
        res = 0

        # two pointer approach - left, right
        left = 0

        while left < len(chars):
            # left pointer will point to current character we are looking at

            # right pointer will stretch as far to the right as possible as long as
            # chars[left] == chars[right]
            right = left
            while right < len(chars) and chars[left] == chars[right]:
                right += 1

            # res will point to start of current character group in chars array
            chars[res] = chars[left]

            # length of compressed group for current character
            currGroupLen = right - left

            # update res since at least the currGroupLen will be 1 (character by itself)
            res += 1

            # if currGroupLen is greater than 1 then we must insert a number into the array
            if currGroupLen > 1:
                # len(str(currGroupLen)) will give us number of digits to insert into array
                # list(str(currGroupLen)) will give us the list that will be inserted into array
                chars[res : res + len(str(currGroupLen))] = list(str(currGroupLen))
                res += len(str(currGroupLen))

            # move left pointer to next character
            left += currGroupLen

        # res will then point past the end of compressed string (length of compressed chars array)
        return res
        