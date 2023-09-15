from collections import deque

MAX = 110
line = [[False for _ in range(MAX)] for _ in range(MAX)]
path = [[False for _ in range(MAX)] for _ in range(MAX)]
rectangle = []
itemX = 0 
itemY = 0
INF = 987654321

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def check_line(x1, y1, x2, y2) :
    for x in range(x1, x2+1) :
        line[x][y1] = True
        line[x][y2] = True
    for y in range(y1, y2+1) :
        line[x1][y] = True
        line[x2][y] = True
        
def is_path(x,y) :
    if not line[x][y] : return False
    
    for x1,y1, x2,y2 in rectangle :
        if x1 < x < x2 and y1 < y < y2 : return False
    return True
            

def bfs(x, y) :
    visited = [[-1 for _ in range(MAX)] for _ in range(MAX)]
    q = deque([[x,y]])
    visited[x][y] = 0
    
    while q :
        cx, cy = q.popleft()
        if cx == itemX and cy == itemY : 
            return visited[cx][cy]
        for i in range(4) :
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not path[nx][ny] or visited[nx][ny] != -1 : continue
            visited[nx][ny] = visited[cx][cy] + 1
            q.append([nx,ny])
            
    return -1
        

def solution(rectangle_, characterX, characterY, itemX_, itemY_):
    global line, path, rectangle, itemX, itemY
    itemX = itemX_*2
    itemY = itemY_*2
    for x1,y1,x2,y2 in rectangle_ :
        rectangle.append([x1*2, y1*2, x2*2, y2*2])
        
    for x1,y1,x2,y2 in rectangle :
        check_line(x1,y1, x2,y2)
        
    for x in range(1, MAX) :
        for y in range(1, MAX) :
            path[x][y] = is_path(x,y)        
    return bfs(characterX*2, characterY*2)//2