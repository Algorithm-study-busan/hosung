def solution(players, callings):
    ranks = dict()

    for i, name in enumerate(players) :
        ranks[name] = i
        
    for call in callings :
        rank = ranks[call]
        players[rank], players[rank-1] = players[rank-1], players[rank]
        ranks[players[rank]], ranks[players[rank-1]] = ranks[players[rank-1]], ranks[players[rank]] 
        
    return players
        
        