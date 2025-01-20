class Solution:
    def reverseVowels(self, s: str) -> str:
        idxs = []
        chars = []

        charSet = {'a', 'e', 'i', 'o', 'u'}

        for i, char in enumerate(s) :
            if char.lower() in charSet :
                idxs.append(i)
                chars.append(char)

        chars.reverse()

        ans = list(s)
        for idx, char in zip(idxs, chars) :
            ans[idx] = char
        return ''.join(ans)
        