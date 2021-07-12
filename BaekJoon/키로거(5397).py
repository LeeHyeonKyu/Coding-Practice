import sys
from collections import deque

def main(key_log):
    left_stack = []
    right_queue = deque()
    for log in key_log:
        if log == '-':
            if left_stack:
                left_stack.pop()
        elif log == '<':
            if left_stack:
                right_queue.appendleft(left_stack.pop())
        elif log == '>':
            if right_queue:
                left_stack.append(right_queue.popleft())
        elif log != '\n':
            left_stack.append(log)
    left_stack.extend(right_queue)
    return ''.join(left_stack)

input = sys.stdin.readline
k = int(input())
for _ in range(k):
    print(main(input()))