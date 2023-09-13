from collections import defaultdict
import math

def time_to_int(t) :
    h, m = map(int, t.split(":"))
    return h*60 + m

def cal_time(t1, t2) :
    t1 = time_to_int(t1)
    t2 = time_to_int(t2)
    return t1-t2

def cal_fee(fees, t) :
    if t <= fees[0] : return fees[1]
    else :
        return fees[1] + math.ceil((t-fees[0]) / fees[2]) * fees[3]
    

def solution(fees, records):
    page = dict()
    total_time = defaultdict(int)
    
    for fee in records :
        time, num, status = fee.split()
        if status == 'IN' :
            page[num] = time
        else :
            total_time[num] += cal_time(time, page.pop(num))
            
    for num, time in page.items() :
        total_time[num] += cal_time("23:59", time)
        
    ans = []    
    for num in sorted(total_time.keys()) :
        ans.append(cal_fee(fees, total_time[num]))
        
    return ans