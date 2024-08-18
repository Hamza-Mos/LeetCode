class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # use a hashmap to track the count of each word in the list
        """
        NOTE: you can only use a max of 1 palindrome word (ex: bb) in the string
              in the middle of the string (odd number of words)

              otherwise, you will keep pairing words with their inverses if there is 
              no palindrome word that exists (even number of words)

              WE WANT TO BE GREEDY and pair up words as much as possible

        approach:

        - iterate over all words in the map
        - use a hashmap to track the count of each word you have encountered so far in the list
        - use a counter to track the number of palindrome words
        - there are 2 cases when you encounter a new word:
            - if its inverse exists in the map
                - then decrement the count of the inverse
                - if the word is a palindrome then decrement the count of palindrome words
                - increment the string length by 4 (word + its inverse)

            - if its inverse does not exist in the map
                - check if the word is a palindrome, if yes then increment palindrome count
                - increment its count in the hashmap

        - finally return result length 
            - if there is at least one palindrome leftover then return result length + 2
              (the palindrome will be used in the middle)


        """

        wordCount = defaultdict(int)
        palindromeCount = 0
        res = 0

        for word in words:
            #  case 1: inverse exists
            if word[::-1] in wordCount:
                # check if word is a palindrome
                if word[::-1] == word:
                    palindromeCount -= 1

                # increment result by 4
                res += 4

                # decrement count of the inverse
                wordCount[word[::-1]] -= 1

                # remove from hashmap if count is 0
                if wordCount[word[::-1]] == 0:
                    del wordCount[word[::-1]]

            # case 2: inverse does not exist
            else:
                # check if word is a palindrome
                if word[::-1] == word:
                    palindromeCount += 1

                wordCount[word] += 1

        return res + 2 if palindromeCount > 0 else res
        