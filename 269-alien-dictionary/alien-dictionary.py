class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = {c : [] for word in words for c in word}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            foundDiff = False

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    # preceding character -> next character alphabetically
                    adjList[word1[j]].append(word2[j])
                    foundDiff = True
                    break

            # invalid
            if not foundDiff and len(word1) > len(word2):
                return ""

        
        visited = set() # visited cell for all letters
        path = set() # marks whether or not a letter is in current dfs path
        res = []

        # returns True if there is a cycle
        # false otherwise
        def dfs(letter):
            if letter in path:
                return True

            if letter in visited:
                return False

            path.add(letter)
            visited.add(letter)

            for c in adjList[letter].copy():
                if dfs(c):
                    return True

            # add letter after visiting all of its children
            res.append(letter)

            path.remove(letter)

            return False

        for char in adjList.keys():
            if dfs(char):
                return ""

        return "".join(res[::-1])

            

            
        