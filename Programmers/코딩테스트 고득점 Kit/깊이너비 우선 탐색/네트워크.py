from collections import Counter

def recursive_dfs(v, net_dict, discovered=[]) :
    discovered.append(v)
    for w in net_dict[v] :
        if not w in discovered :
            discovered = recursive_dfs(w, net_dict)
    return discovered


def solution(n, computers):
    '''
    n : 1~200
    comp : 0~n-1 int
    if i conn j : comp[i][j]=1
    comp[i][i]=1
    answer = num of networks
    '''
    answer = 0
    net_dict = {}
    net_count = []

    for net_idx, net in enumerate(computers) :
        com_net = []
        for com_idx, com in enumerate(net) :
            if com_idx == net_idx :
                pass
            elif com == 1 :
                com_net.append(com_idx)
                pass
            net_dict[net_idx] = com_net
    
    for v in range(n) :
        v_net = set(recursive_dfs(v, net_dict))
        if v_net in net_count :
            pass
        else :
            net_count.append(v_net)
        
        
    answer = len(net_count)
    
    return answer
