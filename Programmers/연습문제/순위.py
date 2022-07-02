class Node():
    def __init__(self):
        self.win = set()
        self.lose = set()

def solution(n, results):
    answer = 0
    people = dict()
    for i in range(1, n+1):
        people[i] = Node()
    
    for winner, loser in results:
        people[winner].win.add(loser)
        people[loser].lose.add(winner)
        people[winner].win |= people[loser].win
        people[loser].lose |= people[winner].lose
        
        for over_winner in people[winner].lose:
            people[over_winner].win |= people[winner].win
        for over_loser in people[loser].win:
            people[over_loser].lose |= people[loser].lose
        
    for person in people.values():
        if len(person.win) + len(person.lose) == n - 1:
            answer += 1
    return answer