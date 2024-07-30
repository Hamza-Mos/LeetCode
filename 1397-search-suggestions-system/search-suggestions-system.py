class TrieNode:
    def __init__(self):
        self.words = []
        self.children = {}

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        res = []

        # functions for trie
        def insertWord(word):
            node = root
            node.words.append(word)

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]
                node.words.append(word)

        for product in products:
            insertWord(product)

        index = 0

        while index < len(searchWord):
            char = searchWord[index]

            if char in root.children:
                root = root.children[char]
                print(char, root.words, root.children)
                res.append(sorted(root.words)[:3])

            else:
                break

            index += 1

        while index < len(searchWord):
            res.append([])
            index += 1

        return res

                
            
        