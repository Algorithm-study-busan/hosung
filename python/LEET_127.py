from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        wordSet = set(wordList)
        if endWord not in wordSet : return 0 
        
        begin = dict()
        beginQ = deque([beginWord])
        begin[beginWord] = 1 

        end = dict()
        endQ = deque([endWord])
        end[endWord] = 1

        while beginQ or endQ :
            tmpQ = deque()
            while beginQ :
                cur = beginQ.popleft()

                for i in range(len(cur)) :
                    for c in string.ascii_lowercase :
                        nxt = cur[:i] + c + cur[i+1:]

                        if nxt in wordSet and nxt not in begin :
                            if nxt in end :
                                return begin[cur] + end[nxt]
                            else :
                                begin[nxt] = begin[cur]+1
                                tmpQ.append(nxt)
            beginQ = tmpQ

            tmpQ = deque()
            while endQ :
                cur = endQ.popleft()

                for i in range(len(cur)) :
                    for c in string.ascii_lowercase :
                        nxt = cur[:i] + c + cur[i+1:]

                        if nxt in wordSet and nxt not in end :
                            if nxt in begin :
                                return end[cur] + begin[nxt]
                            else :
                                end[nxt] = end[cur]+1
                                tmpQ.append(nxt)
            endQ = tmpQ

        return 0