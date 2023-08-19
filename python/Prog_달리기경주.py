def solution(players, callings):
    ranks = dict()

    for i, name in enumerate(players) :
        ranks[name] = i
        
    for call in callings :
        rank = ranks[call]
        players[rank], players[rank-1] = players[rank-1], players[rank]
        rank[players[rank]], rank[players[rank-1]] = rank[players[rank-1]], rank[players[rank]] 
        
    
d = {
    "a" : 1,
    "b" : 2,
}

d["a"], d['b'] = d['b'], d['a']
print(d)
        
        