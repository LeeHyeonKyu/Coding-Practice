_, target = list(map(int, input().split()))
nums = list(map(int, input().split()))
print(sorted(nums)[target-1])