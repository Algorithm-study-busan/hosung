discount = [10, 20, 30, 40]
results = []

def get_price(user_discount, emo, selected_discount) :
    ret = 0
    for i in range(len(emo)) :
        if user_discount <= selected_discount[i] :
            ret += emo[i] * (100- selected_discount[i]) / 100
    return int(ret)
            
    

def get_total(users, emo, selected_discount) :
    ret = [0, 0]
    for user in users :
        price = get_price(user[0], emo, selected_discount)
        print(user, price)  
        if price >= user[1] :
            ret[0] += 1
        else :
            ret[1] += price
    return ret
        
    
    

def brute_force(emo, selected_discount, idx, users) :
    global results
    if idx == len(emo) :
        results.append(get_total(users, emo, selected_discount))
        return
        
    for d in discount :
        selected_discount.append(d)
        brute_force(emo, selected_discount, idx+1, users)
        selected_discount.pop()

def solution(users, emoticons):
    brute_force(emoticons, [], 0, users)
    results.sort(key = lambda x : [-x[0], -x[1]])
    return results[0]

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
# print(solution(users, emoticons))
print(get_total(users, emoticons, [30, 40]))