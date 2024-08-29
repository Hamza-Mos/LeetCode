# ["FileSystem","mkdir","ls","ls","mkdir","ls","ls","addContentToFile","ls","ls","ls"]
# [[],["/goowmfn"],["/goowmfn"],["/"],["/z"],["/"],["/"],["/goowmfn/c","shetopcy"],["/z"],["/goowmfn/c"],["/goowmfn"]]
# [null,null,[],["goowmfn"],null,["goowmfn","z"],["goowmfn","z"],null,[],["/goowmfn/c"],["c"]]
# [null,null,[],["goowmfn"],null,["goowmfn","z"],["goowmfn","z"],null,[],["c"],["c"]]

"""

"""

class TrieNode:
    def __init__(self):
        self.children = {}

class FileSystem:

    def __init__(self):
        self.files = defaultdict(str) # maps file paths to their contents
        self.root = TrieNode()
        

    def ls(self, path: str) -> List[str]:
        # path
        if path in self.files:
            return [path.split("/")[-1]]

        # root directory
        if path == "/":
            return sorted(list(self.root.children.keys()))

        curr = self.root
        directories = path.split("/")[1:]

        for directory in directories:
            if directory not in curr.children:
                curr.children[directory] = TrieNode()

            curr = curr.children[directory]

        return sorted(list(curr.children.keys()))
        

    def mkdir(self, path: str) -> None:
        curr = self.root
        directories = path.split("/")[1:]

        for directory in directories:
            if directory not in curr.children:
                curr.children[directory] = TrieNode()

            curr = curr.children[directory]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        # file not in trie
        if filePath not in self.files:
            self.mkdir(filePath)
            
        self.files[filePath] += content

        

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)