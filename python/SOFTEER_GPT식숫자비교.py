import sys

class Node :
    def __init__(self, n) :
        self.n = n

    def __lt__(self, other) :
        a = self.n.split('.')
        b = other.n.split('.')

        if int(a[0]) < int(b[0]) : return True
        elif int(a[0]) > int(b[0]) : return False
        else :
            if len(a) < len(b) : return True
            elif len(a) > len(b) : return False
            else :
                if len(a) == 2 : return int(a[1]) < int(b[1])

N = int(input())

arr = []

for _ in range(N) :
    arr.append(Node(input()))
arr.sort()

for node in arr :
    print(node.n)
    