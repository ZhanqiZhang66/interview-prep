class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        from collections import defaultdict
        patterns = defaultdict(list)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                patterns[pattern].append(word)
        
        q = deque([beginWord])
        visited = set()
        res = 1

        while q:
            for _ in range(len(q)):
                pop = q.popleft()
                if pop == endWord:
                    return res
                visited.add(pop)
                for j in range(len(pop)):
                    pattern = pop[:j] + "*" + pop[j+1:]
                    for word in patterns[pattern]:
                        if word not in visited:
                            q.append(word)
            res += 1
        return 0
        