from collections import defaultdict

def solution(records):
    result = []
    uid_dict = defaultdict(str)
    for record in records:
        splited_record = record.split()
        if len(splited_record) == 2:
            action, uid = splited_record
            result.append((uid, '님이 나갔습니다.'))
        else:
            action, uid, nickname = splited_record
            uid_dict[uid] = nickname
            if action == 'Enter':
                result.append((uid, '님이 들어왔습니다.'))

    return [uid_dict[uid]+string for uid, string in result]