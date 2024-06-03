from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)

        for s in strs :
            sorted_s = ''.join(sorted(list(s)))
            ana[sorted_s].append(s)

        ans = []

        for a in ana.values() :
            ans.append(a)

        return ans
        