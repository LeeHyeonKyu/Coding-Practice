def solution(land):
    answer = []
    length = len(land)
    
    def dfs(row_idx, prev_idx, val):
        if row_idx == length:
            return val
        
        result = val
        for idx, tmp_val in enumerate(land[row_idx]):
            if idx != prev_idx:
                result = max(dfs(row_idx+1, idx, val+tmp_val), result)
        return result
    
    return dfs(0, 5, 0)

solution([[1,2,3,5],[5,6,7,8]])