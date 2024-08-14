class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        # vals of each character in alphabet
        charVals = [float('inf')] * 26
        
        # set 
        for i in range(len(chars)):
            charVals[ord(chars[i]) - ord('a')] = vals[i]
        
        for i in range(26):
            if charVals[i] == float('inf'):
                charVals[i] = i + 1
        
        ans = 0
        currSum = 0
        
        for i in range(len(s)):
            currSum += charVals[ord(s[i]) - ord('a')]
            ans = max(ans, currSum)
            
            if currSum < 0:
                currSum = 0
        
        return ans