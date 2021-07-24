sentence = input()
target = input()
s_len = len(sentence)
t_len = len(target)
cnt = 0
idx = 0

while idx <= s_len-t_len:
    if sentence[idx : idx+t_len] == target:
        cnt += 1
        idx += t_len
    else:
        idx += 1

print(cnt)