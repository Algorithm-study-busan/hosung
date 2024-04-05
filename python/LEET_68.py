class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        temp_arr = []
        word_sum = 0
        ans = []

        for word in words :
            if word_sum + len(word) <= maxWidth :
                word_sum += len(word) + 1
                temp_arr.append(word)
            else :
                if len(temp_arr) == 1 :
                    s = temp_arr[0]
                    ans.append(s + ' ' * (maxWidth - len(s)) )
                else :
                    len_sum = 0
                    for temp in temp_arr : len_sum += len(temp)
                    space = maxWidth - len_sum
                    div = space // (len(temp_arr) - 1)
                    k = space % (len(temp_arr) - 1)

                    s = ""
                    for temp in temp_arr[:-1] :
                        s += temp
                        s += " "*div
                        if k > 0 : 
                            s += " "
                            k -= 1
                    s += temp_arr[-1]
                    ans.append(s)
                temp_arr = [word]
                word_sum = len(word)+1
        
        if temp_arr :
            s = ' '.join(temp_arr)
            ans.append(s + ' ' * (maxWidth - len(s)) )
                
        return ans

        