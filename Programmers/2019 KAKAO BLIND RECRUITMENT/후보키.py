from copy import deepcopy

def solution(relation):
    n_row, n_col = len(relation), len(relation[0])
    answers = []
    
    def combine_cols(n_combination, num, com_set):
        if len(com_set) == n_combination:
            combinations.append(com_set)
            return
        
        for i in range(num, n_col):
            com_set.add(i)
            if not any(list(map(lambda x: x.issubset(com_set), answers))):
                combine_cols(n_combination, i+1, deepcopy(com_set))
            com_set.discard(i)
    
    for n_combination in range(1, n_col+1):
        combinations = []
        combine_cols(n_combination, 0, set())
        
        for com_set in combinations:
            comb_result = set()
            for data in relation:
                tmp = []
                for key in list(com_set):
                    tmp.append(data[key])
                comb_result.add(tuple(tmp))
            
            if len(comb_result) == n_row:
                answers.append(com_set)
                
    return len(answers)