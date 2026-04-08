class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(wordList)):
                pattern = word[:j] + "*" + word[j + 1: ] #makes whatever that j postion was to "*"
                nei[pattern].append(word) #map any word that fits current pattern to adj list
            
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1: ] #we need to get the wildcards for the word we are at to find neighbors
                    for neiword in nei[pattern]: #then run regular bfs
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            
            res += 1 #found another path to the letter we wnat
    
        return 0 #if we don't ever hit word == endWord just return 0 we never got the word. 