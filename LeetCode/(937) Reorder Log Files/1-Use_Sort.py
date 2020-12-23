class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_lst = []
        dig_lst = []
        
        for log in logs :
            if log.split()[1].isalpha() :
                let_lst.append(log)
            else : 
                dig_lst.append(log)
        
        let_lst.sort(key=lambda x : (x.split()[1:], x.split()[0]))
        
        return let_lst + dig_lst

'''
Runtime : 36 ms
Memory : 14.3 MB
'''
