sell_set = [[r*50 + c for c in range(50)] for r in range(50)]
sell_data = [[0 for _ in range(50)] for _ in range(50)]

def update1(r,c, value) :
    set_idx = sell_set[r][c]
    for i in range(50) :
        for j in range(50) :
            if sell_set[i][j] == set_idx :
                sell_data[r][c] = value

def update2(v1, v2) :
    for i in range(50) :
        for j in range(50) :
            if sell_data[i][j] == v1 :
                sell_data[i][j] = v2
                
def merge(r1, c1, r2, c2) :
    if not sell_data[r1][c1] and sell_data[r2][c2] :
        data = sell_data[r2][c2]
        new_set = sell_set[r2][c2]
        merged_set = sell_set[r1][c1]
    else :
        data = sell_data[r1][c1]
        new_set = sell_set[r1][c1]
        merged_set = sell_set[r2][c2]
        
    for i in range(50) :
        for j in range(50) :
            if sell_set[i][j] == merged_set :
                sell_set[i][j] = new_set
                sell_data[i][j] = data
                
def unmerge(r,c) :
    unmerge_set = sell_set[r][c]
    data = sell_data[r][c]
    
    for i in range(50) :
        for j in range(50) :
            if sell_set[i][j] == unmerge_set :
                sell_set[i][j] = i * 50 + j
                sell_data[i][j] = 0
    sell_data[r][c] = data
    

    


def solution(commands):
    ans = []
    for command in commands :
        cmd_lst = command.split()
        if cmd_lst[0] == 'UPDATE'  :
            if len(cmd_lst) == 4 :
                update1(int(cmd_lst[1])-1, int(cmd_lst[2])-1, cmd_lst[3])
            else :
                update2(cmd_lst[1], cmd_lst[2])
        elif cmd_lst[0] == 'MERGE' :
            r1 = int(cmd_lst[1])-1
            c1 = int(cmd_lst[2])-1
            r2 = int(cmd_lst[3])-1
            c2 = int(cmd_lst[4])-1
            if r1 == r2 and c1 == c2 : continue
            merge(r1,c1,r2,c2)
        elif cmd_lst[0] == 'UNMERGE' :
            r = int(cmd_lst[1])-1
            c = int(cmd_lst[2])-1
            unmerge(r,c)
        elif cmd_lst[0] == 'PRINT' :
            r = int(cmd_lst[1])-1
            c = int(cmd_lst[2])-1
            if sell_data[r][c] : ans.append(sell_data[r][c])
            else : ans.append("EMPTY")

        print(command)
        for i in range(4) :
            print(*sell_data[i][:4])
        print()
        for i in range(4) :
            print(*sell_set[i][:4])
        print()
        
    return ans
            
solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])