from collections import deque

def solution(N, number):
    queue = deque()
    queue.append([[str(N)], 1]) # formula, step
    operators = ['*', '+' , '//']
    
    def calc_formula(formula, results):
        if len(formula) == 1:
            return {formula[0]}
        
        for idx, unit in enumerate(formula):
            if unit in operators:
                tmp_result = eval(''.join(formula[idx-1:idx+2]))
                result = calc_formula(formula[:idx-1] + [str(tmp_result)] + formula[idx+2:], results)
                results |= result
        return results
    
    while queue:
        formula, step = queue.popleft()
        results = calc_formula(formula, set())
        if number in results:
            return step
        
        if step <= 8:
            for operator in operators:
                queue.append((formula + [operator, str(N)], step+1))
            formula[-1] = formula[-1] + str(N)
            queue.append((formula, step+1))
        else:
            return -1

solution(5, 12)