import sys

def main(lst, length, target):
    answer = 0
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1,length):
                num = lst[i] + lst[j] + lst[k]
                if num <= target:
                    answer = max(answer, num)
    return answer

input = sys.stdin.readline
length, target = list(map(int, input().split()))
lst = list(map(int, input().split()))
print(main(lst, length, target))