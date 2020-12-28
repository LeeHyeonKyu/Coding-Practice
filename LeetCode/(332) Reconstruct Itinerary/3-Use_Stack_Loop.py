class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프 구성
        graph = collections.defaultdict(list)
        for start, end in sorted(tickets) :
            graph[start].append(end)

        route, stack = [], ['JFK']
        while stack :
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]] :
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        
        # 뒤집어서 결과 반환
        return route[::-1]

'''
Runtime : 76 ms
Memory : 14.3 MB
'''
