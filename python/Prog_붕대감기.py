def solution(bandage, health, attacks):
    need_time, plus_per_seconds, plus_success = bandage
    hp = health
    max_hp = health

    last_attack_time = attacks[-1][0]
    attack = [0 for _ in range(last_attack_time+1)]
    
    for t,d in attacks :
        attack[t] = d
    
    success_cnt = 0
    for t in range(last_attack_time+1) :
        if attack[t] :
            hp -= attack[t]
            if hp <= 0 : return -1
            success_cnt = 0
        else :
            success_cnt += 1
            hp = min(max_hp, hp + plus_per_seconds)
            if success_cnt == need_time :
                success_cnt = 0
                hp = min(max_hp, hp + plus_success)
    
    return hp