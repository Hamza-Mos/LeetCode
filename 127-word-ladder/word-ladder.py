class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = collections.defaultdict(list)

        for w in wordList:
            for j in range(len(w)):
                currWord = w[:j] + "*" + w[j + 1:]
                adjList[currWord].append(w)

        print(adjList)

        queue = deque([beginWord])
        visited = {beginWord} # set

        res = 1 # length of transformation sequence

        while queue:
            currLevelLen = len(queue)
            
            for i in range(currLevelLen):
                currWord = queue.popleft()

                if currWord == endWord:
                    return res

                for j in range(len(currWord)):
                    pattern = currWord[:j] + "*" + currWord[j + 1:]
                    for word in adjList[pattern]:
                        if word not in visited:
                            queue.append(word)
                            visited.add(word)

            res += 1

        return 0

            
        