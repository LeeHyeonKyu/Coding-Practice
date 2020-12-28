class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        route = []
        
        # 그래프 거꾸로 구성
        for start, end in sorted(tickets, reverse=True) :
            graph[start].append(end)
        
        def dfs(departure) :
            # 마지막 값을 읽어 어휘 순 방문
            while graph[departure] :
                dfs(graph[departure].pop())
            route.append(departure)
            pass # end dfs
        
        dfs('JFK')
        # 역순으로 뒤집어 결과 값 생성
        return route[::-1]

'''
Runtime : 68 ms
Memory : 14.5 MB
'''
