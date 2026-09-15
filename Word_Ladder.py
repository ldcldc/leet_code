from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append(beginWord)
        
        wordList = set(wordList)
        
        if endWord not in wordList:
            return 0
        
        count = 1
        while(queue):
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return count
                for i in range(len(curr_word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        temp = curr_word[:i] + c + curr_word[i+1:]
                        if temp in wordList:
                            queue.append(temp)
                            wordList.remove(temp)
            count += 1
            
        return 0
    
a = Solution()
#print(a.ladderLength("a", "c", ["a","b","d","c"]))
print(a.ladderLength("hit", "cog", ["hot","dot","dog","log","lot","cog"]))