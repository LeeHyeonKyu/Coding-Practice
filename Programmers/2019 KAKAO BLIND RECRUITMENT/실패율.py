from collections import Counter
import heapq

def solution(N, stages) :
	stages = sorted(stages)
	cnt_stages = Counter(stages)
	heap = []

	for stage in range(1, N+1) :
		if stage in cnt_stages :
			heapq.heappush(heap, (-cnt_stages[stage]/len(stages), stage))
		else :
			heapq.heappush(heap, (0, stage))
		stages = stages[cnt_stages[stage]:]
	
	answer = []
	while heap :
		rate, stage = heapq.heappop(heap)
		answer.append(stage)
	
	return answer
