def solution(n) :
    # 층 별 list 초기화
    map_dict = {}
    for i in range(n) :
        map_dict[i] = [0]*(i+1)

    # 조건에 따라 값 채워나가기
    ceiling, floor = 0, n-1
    row, col = 0, 0
    val = 1
    while ceiling <= floor :
        # 아래로 내려가며 값 채우기
        while row < floor :
            map_dict[row][col] = val if map_dict[row][col] == 0 else map_dict[row][col]
            row += 1
            val += 1
        # 우측으로 이동하며 값 채우기
        tmp = (len(map_dict[floor]) - map_dict[floor].count(0)) // 2
        while col < len(map_dict[floor]) - tmp - 1 :
            map_dict[row][col] = val if map_dict[row][col] == 0 else map_dict[row][col]
            col += 1
            val += 1
        # 위로 올라가며 값 채우기
        while row > ceiling :
            map_dict[row][col] = val if map_dict[row][col] == 0 else map_dict[row][col]
            row -= 1
            col -= 1
            val += 1
        # 사이드 조건 처리
        if ceiling == floor and map_dict[row][col] == 0 :
            map_dict[row][col] = val
        # 안쪽 삼각형으로 조건 변경
        ceiling += 2
        floor -= 1
        row += 2
        col += 1

    # 한 리스트에 담아서 return
    answer = []
    for i in range(n) :
        answer.extend(map_dict[i])

    return answer
