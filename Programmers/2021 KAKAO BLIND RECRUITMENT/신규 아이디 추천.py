def solution(new_id):
    suggest_id = []

    new_id = new_id.lower()
    for char in new_id:
        if char.isalnum() or char in {'-', '_'}:
            suggest_id.append(char)
        elif char == '.':
            if len(suggest_id) != 0 and suggest_id[-1] != '.':
                suggest_id.append(char)

    if len(suggest_id) == 0:
        suggest_id.append('a')
    if len(suggest_id) > 15:
        suggest_id = suggest_id[:15]
    if suggest_id[-1] == '.':
        suggest_id.pop()
    while len(suggest_id) < 3:
        suggest_id.append(suggest_id[-1])
    
    return ''.join(suggest_id)