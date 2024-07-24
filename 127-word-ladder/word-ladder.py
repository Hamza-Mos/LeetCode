class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # adjacency list -> map wildcard words to list of words
        adjList = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                adjList[word[:i] + "*" + word[i + 1:]].append(word)
        
        q = deque([[beginWord, 1]])
        visit = set()

        while q:
            word, numRounds = q.popleft()

            if word in visit:
                continue
            visit.add(word)

            for i in range(len(word)):
                wildcard = word[:i] + "*" + word[i + 1:]

                for nextWord in adjList[wildcard]:
                    if nextWord == endWord:
                        print(word)
                        return numRounds + 1
                    if nextWord not in visit:
                        q.append([nextWord, numRounds + 1])

        return 0


        