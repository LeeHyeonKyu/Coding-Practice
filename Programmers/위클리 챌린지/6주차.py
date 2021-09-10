import heapq

def calc_num_wins(i, weights, records):
    num_games = 0
    num_wins = 0
    num_hard_wins = 0
    for idx, record in enumerate(records):
        if record == 'W':
            num_wins += 1
            num_games += 1
            if weights[i] < weights[idx]:
                num_hard_wins += 1
        elif record == 'L':
            num_games += 1
    win_rate = num_wins / num_games if num_games != 0 else 0
    return win_rate, num_hard_wins

def solution(weights, head2head):
    heap = []
    for i in range(len(weights)):
        win_rate, num_hard_wins = calc_num_wins(i, weights, head2head[i])
        weight = weights[i]
        num = i+1
        heapq.heappush(heap, (-win_rate, -num_hard_wins, -weight, num))
    
    answer = []
    while heap:
        _, _, _, num = heapq.heappop(heap)
        answer.append(num)
    return answer