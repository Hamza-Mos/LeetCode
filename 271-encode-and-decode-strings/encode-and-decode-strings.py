class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = ""

        for s in strs:
            output += str(len(s)) + "#" + s

        return output
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []

        index = 0

        while index < len(s):
            lengthOfCurrString = 0

            while s[index].isdigit():
                lengthOfCurrString = lengthOfCurrString * 10 + int(s[index])
                index += 1

            index += 1
            res.append(s[index: index + lengthOfCurrString])

            index += lengthOfCurrString

        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))