arr = ['RR' , 'Rr', 'Rr', 'rr']

def cal(n,p) : 
    if n == 1 : return 'Rr'
    if p <= 4**(n-2) : return 'RR'
    elif p <= 4**(n-1)*3/4 : return arr[(p-1)%4]
    else : return 'rr'

def solution(queries):
    answer = []
    for query in queries :
        answer.append(cal(query[0], query[1]))
    return answer