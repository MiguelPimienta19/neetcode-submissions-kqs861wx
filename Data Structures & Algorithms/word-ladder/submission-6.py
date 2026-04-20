class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if beginWord == endWord:
            return 0
        
        adjlist = defaultdict(list)

        wordList.append(beginWord)
        for word in wordList:
            for char in range(len(word)):
                pattern = word[ :char] + "*" + word[char + 1:]
                adjlist[pattern].append(word)
        
        q, visit = deque([beginWord]), set()
        res = 1 #may need to change to 0

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern =  word[:j] + "*" + word[j + 1:]
                    for neiword in adjlist[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
        
            res += 1 
        return 0 
        


