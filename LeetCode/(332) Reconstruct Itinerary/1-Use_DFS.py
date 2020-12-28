class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        route = []
        
        # 그래프 구성
        for start, end in sorted(tickets) :
            graph[start].append(end)
        
        def dfs(departure) :
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[departure] :
                dfs(graph[departure].pop(0))
            route.append(departure)
            pass # end dfs
        
        dfs('JFK')
        # 역순으로 뒤집어 결과 값 생성
        return route[::-1]

'''
Runtime : 73 ms
Memory : 15 MB
'''
