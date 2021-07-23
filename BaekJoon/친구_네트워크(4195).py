def find(node):
    if node == parent[node]:
        p_node = node
    else:
        p_node = find(parent[node])
        parent[node] = p_node
    return p_node

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        nums[x] += nums[y]

test_case = int(input())

for _ in range(test_case):
    parent = {}
    nums = {}

    f = int(input())
    for _ in range(f):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            nums[x] = 1
        if y not in parent:
            parent[y] = y
            nums[y] = 1

        union(x, y)
        print(nums[find(x)])