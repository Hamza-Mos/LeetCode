class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordList = []

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insertWord(word)

    def insertWord(self, word):
        curr = self.root
        curr.wordList.append(word)

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
            curr.wordList.append(word)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie(products)
        currNode = trie.root
        res = []

        for char in searchWord:
            if char not in currNode.children:
                break
            
            currNode = currNode.children[char]
            res.append(sorted(currNode.wordList)[:3])

        # Fill the remaining slots with empty lists if we broke early
        while len(res) < len(searchWord):
            res.append([])

        return res