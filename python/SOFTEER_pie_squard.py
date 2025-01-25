import sys

class Node :
    def __init__(self, value = None, idx = None, left = None, right = None) :
        self.value = value
        self.idx = idx
        self.left = left
        self.right = right


head = Node()
tail = Node()

N = int(input())
arr = list(map(int, input().split()))

last = head
for i, n in enumerate(arr) :
    node = Node(value = n, idx = i, left = last)
    last.right = node
    last = node

last.right = tail
tail.left  = last

# tmp = head
# while tmp :
#     print(tmp.idx, tmp.value)
#     tmp = tmp.right

while head.right.right != tail :
    tmp = head.right
    while tmp != tail :
        value = tmp.value
        if tmp.left.value != None and tmp.left.value <= value :
            tmp.value += tmp.left.value
            tmp.left = tmp.left.left
            tmp.left.right = tmp
        if tmp.right.value != None and tmp.right.value <= value :
            tmp.value += tmp.right.value
            tmp.right = tmp.right.right
            tmp.right.left = tmp
        tmp = tmp.right

print(head.right.value)
print(head.right.idx+1)


        