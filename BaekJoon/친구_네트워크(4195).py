import sys
from collections import deque, defaultdict

def main(name1, name2):
    queue = deque()
    graph[name1].append(name2)
    graph[name2].append(name1)
    network = set()
    queue.append(name1)
    queue.append(name2)
    network.add(name1)
    network.add(name2)
    while queue:
        person = queue.popleft()
        for friend in graph[person]:
            if friend not in network:
                queue.append(friend)
                network.add(friend)
    return len(network)

input = sys.stdin.readline
num_test_cases = int(input())
for _ in range(num_test_cases):
    num_input = int(input())
    graph = defaultdict(list)
    for _ in range(num_input):
        name1, name2 = input().split()
        print(main(name1, name2))