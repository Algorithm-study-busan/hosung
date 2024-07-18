from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        s = deque(sandwiches)

        cnt = [0 for _ in range(len(students)+1)]

        while q :
            if cnt[len(q)] > len(q) : break
            if q[0] == s[0] : 
                q.popleft()
                s.popleft()
            else :
                q.append(q.popleft())
                cnt[len(q)]+=1

        return len(q)
        