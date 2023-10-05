from sys import stdin
input = stdin.readline

mapping = {
    '-' : '0',
    'cpp' : '1', 
    'java' : '2',
    'python' : '3',
    'backend' : '1',
    'frontend' : '2',
    'junior' : '1',
    'senior' : '2',
    'chicken' : '1',
    'pizza' : '2'
}
cnt = [[] for _ in range(10_000)]

def cal_count(arr, x) :
    print(arr, x)
    lo = 0
    hi = len(arr)-1
    
    while lo <= hi :
        mid = (lo + hi)//2
        if arr[mid] >= x : hi = mid-1
        else : lo = mid+1
    
    return len(arr) -lo

def to_code(code_arr) :
    return int(''.join(code_arr))

def count(arr) :
    code_arr = [mapping[arr[0]], mapping[arr[1]], mapping[arr[2]], mapping[arr[3]]]
    x = int(arr[-1])
    
    cnt[to_code(code_arr)].append(x)
    
    print(code_arr)
    print("-----")
    
    for i in range(4) :
        tmp = code_arr[i]
        code_arr[i] = '0'
        print(code_arr)
        cnt[to_code(code_arr)].append(x)
        code_arr[i] = tmp
        
    for i in range(4) :
        for j in range(i+1, 4):
            tmp1 = code_arr[i]
            tmp2 = code_arr[j]
            code_arr[i] = '0'
            code_arr[j] = '0'
            print(code_arr)
            cnt[to_code(code_arr)].append(x)
            code_arr[i] = tmp1
            code_arr[j] = tmp2
            
    for i in range(4) :
        for j in range(i+1,4) :
            for k in range(j+1, 4) :
                tmp1 = code_arr[i]
                tmp2 = code_arr[j]
                tmp3 = code_arr[k]
                code_arr[i] = '0'
                code_arr[j] = '0'
                code_arr[k] = '0'
                print(code_arr)
                cnt[to_code(code_arr)].append(x)
                code_arr[i] = tmp1
                code_arr[j] = tmp2
                code_arr[k] = tmp3
                
    cnt[0].append(x)
    
    
    
    
def solution(info, query):
    ans = []
    
    info_sort = []
    for x in info :
        info_sort.append(x.split())
    info_sort.sort(key=lambda x:int(x[-1]))
    
    print(info_sort)
    
    for arr in info_sort :
        count(arr)
        
    for q in query :
        q_split = list(map(str.strip, q.split('and')))
        # print(q_split)
        x = int(q_split[-1].split()[1])
        
        code_arr = [mapping[q_split[0]], mapping[q_split[1]], mapping[q_split[2]], mapping[q_split[3].split()[0]]]
        code = to_code(code_arr)
        print(code)
        ans.append(cal_count(cnt[code], x))
        
    return ans
    
    
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
    