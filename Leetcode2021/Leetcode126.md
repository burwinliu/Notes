# Leetcode126.md
Typical BFS problem -- just need to be careful with the graph construction (messed up once due to letters being improperly formatted) -- 127 is a really similar problem (not sure why 2 comes before 1...)
```
letters = [
    'a','b','c','d','e','f','g',
    'h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u',
    'v','w','x','y','z'
]

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Construct the graph
        wordList.append(beginWord)
        graph = self.buildGraph(wordList)
        # Check if graph is valid for this operation
        if endWord not in graph:
            return []
        # If a word is reached already in the past, discard -- as we know its been reached earlier, and therefore this path is no good
        traversed = set([beginWord])
        searchSet = [[beginWord]]
        res = []
        while len(searchSet) != 0:
            nextSet = []
            newTraversed = set()
            for cur in searchSet:
                for target in graph[cur[-1]]:
                    if target in traversed:
                        continue
                    newEntry = [v for v in cur]
                    newEntry.append(target)
                    newTraversed.add(target)
                    if target == endWord:
                        res.append(newEntry)
                    nextSet.append(newEntry)
            if len(res) != 0:
                return res
            searchSet = nextSet
            for t in newTraversed:
                traversed.add(t)
        return []
                        
        
    def buildGraph(self, ls: List[str]):
        res = {}
        setLs = set(ls)
        for word in ls:
            res[word] = set()
            for index in range(len(word)):
                for letter in letters:
                    candidateWord = word[:index] + letter + word[index+1:] 
                    if candidateWord in setLs and candidateWord != word:
                        res[word].add(candidateWord)
        return res
```