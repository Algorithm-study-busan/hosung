from collections import deque

def solution(order):
    boxes = deque([n for n in range(1, len(order)+1)])
    q = deque(order)
    stck = []
        
    while q :
        od = q[0]
        print(q)
        if len(boxes) != 0 and boxes[0] == od :
            boxes.popleft()
            q.popleft()
        elif len(stck) != 0 and stck[-1] == od :
            stck.pop()
            q.popleft()
        elif len(boxes) != 0 and boxes[0] != od :
            stck.append(boxes.popleft())
        else :
            break
        
    return len(order) - len(q)
        
print(solution([4, 3, 1, 2, 5]))
