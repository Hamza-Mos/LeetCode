# Trie solution

class TrieNode:
    def __init__(self):
        # children nodes
        self.children = {} # maps a directory to another trienode
        self.isFile = False

        # files contain content
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = TrieNode() # root directory: /
        

    def ls(self, path: str) -> List[str]:
        # root directory
        if path == "/":
            return sorted(list(self.root.children.keys()))

        path = path.split("/")[1:] # removes the empty string in the beginning
        curr = self.root

        for directory in path:
            if directory not in curr.children:
                curr.children[directory] = TrieNode()

            curr = curr.children[directory]

        # case where path is a file path
        if curr.isFile:
            return [path[-1]]

        directoryList = list(curr.children.keys())

        return sorted(directoryList)
        

    def mkdir(self, path: str) -> None:
        path = path.split("/")[1:] # removes the empty string in the beginning
        curr = self.root

        for directory in path:
            if directory not in curr.children:
                curr.children[directory] = TrieNode()

            curr = curr.children[directory]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split("/")[1:] # removes the empty string in the beginning
        curr = self.root

        for directory in path:
            if directory not in curr.children:
                curr.children[directory] = TrieNode()

            curr = curr.children[directory]
        
        curr.isFile = True
        curr.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split("/")[1:] # removes the empty string in the beginning
        curr = self.root

        for directory in path:
            if directory not in curr.children:
                curr.children[directory] = TrieNode()

            curr = curr.children[directory]
        
        return curr.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)