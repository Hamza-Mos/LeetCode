class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        approach:

        - we want to be greedy and fit as many words as possible for each line
        - we will keep track of each line using an array and keep track of each line's length
        - if the line is complete (meaning that we cannot fit another word), then we will insert
          spaces between the words on the current line (including remainder spaces if its not even)
          then append the line to the result list

        - else, we will continue to fit words until we complete the line

        - for the last line, we will only append extra spaces to the end of the line
        """

        currLine, currLineLength = [], 0

        wordIndex = 0
        res = []

        while wordIndex < len(words):
            # case 1: line is complete
            # len(currLine) would represent number of min spaces (1 space) between words
            # once words[wordIndex] gets added
            if currLineLength + len(currLine) + len(words[wordIndex]) > maxWidth:
                # add spaces to the line
                extraSpaces = maxWidth - currLineLength

                # single word
                if len(currLine) == 1:
                    # remainderSpaces should be 0 since we are dividing by 1 word (always divides evenly)
                    res.append(currLine[0] + (" " * extraSpaces))

                else:
                    # spaces divided by words evenly
                    spacesPerWord = extraSpaces // (len(currLine) - 1)
                    # remainder spaces
                    remainderSpaces = extraSpaces % (len(currLine) - 1)

                    # add spaces to each word (except last word)
                    for j in range(0, len(currLine) - 1):
                        currLine[j] += " " * spacesPerWord

                        if remainderSpaces > 0:
                            currLine[j] += " "
                            remainderSpaces -= 1

                    res.append("".join(currLine))

                # reset variables
                currLine, currLineLength = [], 0 

                # wordIndex remains the same since we have not added words[wordIndex]
                continue

            # case 2: line is incomplete (can fit more words in)
            else:
                currLine.append(words[wordIndex])
                currLineLength += len(words[wordIndex])
                wordIndex += 1

        # last line
        lastLine = " ".join(currLine)
        lastLineLength = len(lastLine)

        # always add spaces to end of last line
        extraSpaces = maxWidth - lastLineLength
        lastLine += " " * extraSpaces

        res.append(lastLine)

        return res