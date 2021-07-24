def calc(formula):
    formula = ''.join(formula.split())
    result = eval(formula)
    return True if result == 0 else False

def main(num):
    lst = []
    def recursive(formula, n):
        n += 1
        if n > num:
            if calc(formula):
                lst.append(formula)
            return
        recursive(f'{formula} {n}', n)
        recursive(f'{formula}+{n}', n)
        recursive(f'{formula}-{n}', n)
    recursive('1', 1)
    return lst

num_cases = int(input())
for i in range(num_cases):
    answer_lst = main(int(input()))
    for answer in answer_lst:
        print(answer)
    print()