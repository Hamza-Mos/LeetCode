class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # maps a pattern to list of words that match that pattern ('*' is a wildcard)
        adjList = collections.defaultdict(list)

        # generate and populate the adjacency list
        for w in wordList:
            for j in range(len(w)):
                currWord = w[:j] + "*" + w[j + 1:]
                adjList[currWord].append(w)

        # start with the beginWord
        queue = deque([beginWord])
        visited = {beginWord} # set

        res = 1 # length of transformation sequence

        # bfs
        while queue:
            currLevelLen = len(queue)
            
            # loop over all words in the current level
            for i in range(currLevelLen):
                currWord = queue.popleft()

                # if we reached end word then return result
                if currWord == endWord:
                    return res

                # otherwise generate all possible patterns of current word
                for j in range(len(currWord)):
                    pattern = currWord[:j] + "*" + currWord[j + 1:]

                    # loop over all words matching the current pattern
                    for word in adjList[pattern]:
                        # if word has not been visited yet then add it to queue and mark it as visited
                        if word not in visited:
                            queue.append(word)
                            visited.add(word)

            # increment length of transformation sequence
            res += 1

        return 0

            
        