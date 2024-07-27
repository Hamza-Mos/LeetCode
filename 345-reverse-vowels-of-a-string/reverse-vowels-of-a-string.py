class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        seen = []

        # Collect vowels
        for c in s:
            if c in vowels:
                seen.append(c)

        # Reverse the list of vowels
        seen.reverse()

        index = 0
        newStr = ""
        for i in range(len(s)):
            if s[i] in vowels:
                newStr += seen[index]
                index += 1
            else:
                newStr += s[i]

        return newStr
