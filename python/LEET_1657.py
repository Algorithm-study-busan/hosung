from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) : return False

        word1_d = defaultdict(int)
        word2_d = defaultdict(int)

        for i in range(len(word1)) :
            word1_d[word1[i]] += 1
            word2_d[word2[i]] += 1
        
        return word1_d.keys() == word2_d.keys() and sorted(list(word1_d.values())) == sorted(list(word2_d.values()))
