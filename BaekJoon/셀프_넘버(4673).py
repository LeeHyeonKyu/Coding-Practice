def adder(num: int) -> int:
    for n in str(num):
        num += int(n)
    return num

def main() -> None:
    checker = [False] + ([True] * 10000)
    i = 1
    while i <= 10000:
        result = adder(i)
        if result <= 10000:
            checker[result] = False
        i += 1
    
    for idx, flag in enumerate(checker):
        if flag:
            print(idx)

main()