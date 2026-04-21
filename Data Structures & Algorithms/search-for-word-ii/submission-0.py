class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a trie from words
        root = Trie()
        for word in words:
            root.insert(word)

        # backtrack on board
        # record matches
        R, C = len(board), len(board[0])
        res = set()
        visited = set()
        DIRs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def backtrack(r, c, curr, word):
            if r not in range(R) or c not in range(C) or board[r][c] not in curr.children or (r, c) in visited:
                return

            visited.add((r, c))
            word = word + board[r][c]
            curr = curr.children[board[r][c]]
            if curr.isEnd:
                res.add(word)

            for dr, dc in DIRs:
                rr, cc = r + dr, c + dc
                backtrack(rr, cc, curr, word)
            visited.remove((r, c))



        for r in range(R):
            for c in range(C):
                backtrack(r, c, root, "")
        return list(res)
        


        