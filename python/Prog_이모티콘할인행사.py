users = []
emos = []
ans = []

discounts = [10, 20, 30, 40]

def cal_ans(sales) :
    total_price = 0
    primeum = 0
    
    for user in users :
        price = 0
        for emo, sale in zip(emos, sales) :
            if sale >= user[0] :
                price += emo * (100-sale)/100
        if price >= user[1] :
            primeum += 1
        else :
            total_price += price
            
    return [primeum, total_price]
        

def brute_force(sales) :
    if len(sales) == len(emos) :
        ans.append(cal_ans(sales))
        return
    for discount in discounts : 
        sales.append(discount)
        brute_force(sales)
        sales.pop()
        
        

def solution(u, emoticons):
    global users, emos, ans
    users = u
    emos = emoticons
    
    brute_force([])
    
    ans.sort(key=lambda x : (-x[0], -x[1]))
    
    return ans[0]