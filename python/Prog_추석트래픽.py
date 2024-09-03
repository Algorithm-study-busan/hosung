def solution(lines):
    def timeToInt(time) :
        ret = 0
        h,m,s = time.split(':')
        ret += int(h)*60*60*1000
        ret += int(m)*60*1000
        ret += int(float(s)*1000)
        return ret
    
    def sToInt(s) :
        return int(float(s[:-1])*1000)
    
    arr = []
    for x in lines :
        date, time, s = x.split()
        endTime = timeToInt(time)
        startTime = endTime - sToInt(s)+1
        arr.append([startTime, endTime])
        
    ans = 0
    for i in range(len(arr)) :
        tmp = 1
        for j in range(i+1, len(arr)) :
            if arr[i][1] + 1000 <= arr[j][0] : continue
            tmp += 1
        ans = max(ans,tmp)
    return ans