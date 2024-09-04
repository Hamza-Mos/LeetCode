class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        # avoid duplicates
        words = set(dictionary)
        self.abreviations = defaultdict(list)
        
        for word in words:
            abreviation = self.get_abreviation(word)

            self.abreviations[abreviation].append(word)

    def get_abreviation(self, word: str) -> str:
        abreviation = ""

        if len(word) <= 2:
            abreviation = word

        else:
            abreviation = word[0] + str(len(word) - 2) + word[-1]

        return abreviation
        

    def isUnique(self, word: str) -> bool:
        # 3 cases
        # 1) no other word found -> return True
        # 2) only one other word is found and it is the same word -> return True
        # 3) otherwise, return False

        abreviation = self.get_abreviation(word)

        if len(self.abreviations[abreviation]) == 0:
            return True

        if len(self.abreviations[abreviation]) == 1 and self.abreviations[abreviation][0] == word:
            return True

        return False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)