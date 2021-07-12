N = input()
N_lst = input().split()
N_lst = set(N_lst)
M = input()
M_lst = input().split()

for num in M_lst:
    print(1 if num in N_lst else 0)