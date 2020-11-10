def solution(n, lost, reserve):
    answer = 0
    student_arr = [0] * n

    for i in lost :
        student_arr[i-1] -= 1
        pass

    for i in reserve :
        student_arr[i-1] += 1

    for idx, student in enumerate(student_arr) :
        if student == -1 and idx != 0 :
            if student_arr[idx-1] == 1 :
                student_arr[idx] += 1
                student_arr[idx-1] -= 1
                pass
            pass

        if student == -1 and idx != n-1 :
            if student_arr[idx+1] == 1 :
                student_arr[idx] += 1
                student_arr[idx+1] -= 1
                pass
            pass
        pass # end for

    answer = n - student_arr.count(-1)

    return answer
