class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = chars[0]
        cnt = 1
        for c in chars[1:] :
            if c == ans[-1] :
                cnt += 1
            else :
                ans += ("" if cnt == 1 else str(cnt))
                ans += c
                cnt = 1

        if cnt != 1 : 
            ans += str(cnt)
        
        for i in range(len(ans)) :
            chars[i] = ans[i]
        while len(chars) > len(ans) :
            chars.pop()
        return len(ans)
