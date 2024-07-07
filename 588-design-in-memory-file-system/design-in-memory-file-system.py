class TrieNode:
    def __init__(self):
        self.children = {}
        self.content = ""
        self.isFile = False

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        path = path.split("/")

        curr = self.root

        for p in path:
            if not p:
                continue
            curr = curr.children[p]

        if curr.isFile:
            return [path[-1]]

        else:
            return sorted(list(curr.children.keys()))
        

    def mkdir(self, path: str) -> None:
        path = path.split("/")

        curr = self.root

        for p in path:
            if not p:
                continue

            if p not in curr.children:
                curr.children[p] = TrieNode()

            curr = curr.children[p]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split("/")

        curr = self.root

        for p in path:
            if not p:
                continue

            if p not in curr.children:
                curr.children[p] = TrieNode()

            curr = curr.children[p]

        curr.content += content
        curr.isFile = True
        

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split("/")

        curr = self.root
        
        for p in path:
            if not p:
                continue

            curr = curr.children[p]

        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)