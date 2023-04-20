def is_ancestors_include(node, deleted_node) :
    while node != -1 :
        if node == deleted_node : return True
        node = parent[node]
    return False

n = int(input())
parent = list(map(int, input().split()))
m = int(input())


result = 0
for i in range(n):
  if not is_ancestors_include(i, m) and not i in parent: result += 1

print(result)