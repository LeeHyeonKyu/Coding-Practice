import queue

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = queue.Queue()
    time = 0
    idx = 0
    now_weight = 0

    for _ in range(bridge_length) :
        bridge.put(0)

    while True :
        time += 1

        goalin = bridge.get()
        now_weight -= goalin

        if now_weight + truck_weights[idx] <= weight :
            bridge.put(truck_weights[idx])
            now_weight += truck_weights[idx]
            idx += 1
        else : 
            bridge.put(0)
            pass

        if idx == len(truck_weights) :
            answer = time + bridge_length
            break

    return answer
