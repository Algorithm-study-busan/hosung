def solution(coin, cards):
    T = len(cards)
    N = len(cards)//3
    last_round = N+1
    
    ans = 1
    hand = [False for _ in range(T+1)]
    discard = [False  for _ in range(T+1)]
    for i in range(N) :
        if hand[T+1-cards[i]] : ans += 1
        hand[cards[i]] = True
    
    while coin > 0 and ans < last_round :
        ck = False
        for i in range(N, N+ans*2) : 
            if coin > 0 and hand[T+1-cards[i]] and not discard[cards[i]]:
                discard[cards[i]] = True
                ans += 1
                coin -= 1
                ck = True
                break
        if ck : continue
        
        if coin <= 1 : break
        
        ck = False
        for i in range(N, N+ans*2) :
            if ck : break
            for j in range(i+1, N+ans*2) :
                if cards[i] + cards[j] == T+1 and coin >= 2 and not discard[cards[i]]:
                    discard[cards[i]] = True
                    discard[cards[j]] = True
                    coin -= 2
                    ans += 1
                    ck = True
                    break
        if ck : continue
        
        break;      
                
    return ans