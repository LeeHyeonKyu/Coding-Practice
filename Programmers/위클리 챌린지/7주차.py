from collections import defaultdict

def solution(enter, leave):
    result = [0] * (len(enter)+1)
    room = set()
    enter.reverse()
    for leave_one in leave:
        while leave_one not in room:
            enter_one = enter.pop()
            room.add(enter_one)
        room.discard(leave_one)
        result[leave_one] += len(room)
        for room_in_one in room:
            result[room_in_one] += 1
    
    return result[1:]