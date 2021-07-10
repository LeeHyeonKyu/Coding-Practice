import sys

def main(k, lst):
    answer_lst = []
    stack = []
    idx = 0
    for num in range(1, k+1):
        stack.append(num)
        answer_lst.append('+')
        while stack and idx < len(lst) and stack[-1] == lst[idx]:
            stack.pop()
            answer_lst.append('-')
            idx += 1

    return answer_lst if idx == len(lst) else ['NO']

input = sys.stdin.readline
k = int(input())
lst = []
for _ in range(k):
    lst.append(int(input()))

answer_lst = main(k, lst)
for answer in answer_lst:
    print(answer)