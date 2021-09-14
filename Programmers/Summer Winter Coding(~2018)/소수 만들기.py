import math

def is_prime(num):
    limit = math.ceil(math.sqrt(num))
    for i in range(2, limit+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    tot_len = len(nums)
    for i in range(tot_len):
        for j in range(i+1, tot_len):
            for k in range(j+1, tot_len):
                num = nums[i] + nums[j] + nums[k]
                if is_prime(num):
                    answer += 1
    return answer