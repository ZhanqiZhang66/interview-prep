class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isEnd = True
    
    def search(self, word: str) -> bool:
        
        def dfs(node, start):
            curr = node
            if start == len(word):
                return curr.isEnd
            
            for i in range(start, len(word)):
                c = word[i]
                if c == '.':
                    for children in curr.children.values():
                        if dfs(children, i+1):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    return dfs(curr.children[c], i+1)
        return dfs(self.root, 0)
    


        
        
