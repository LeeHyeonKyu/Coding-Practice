def solution(answers):

    answer = []
    length = len(answers)
    guy1 = str('12345' * ((length//5) + 1))
    guy2 = str('21232425' * ((length//8) + 1))
    guy3 = str('3311224455' * ((length//10) + 1))
    
    guy1_correct = 0
    guy2_correct = 0
    guy3_correct = 0
    
    for idx, num in enumerate(answers) :
        if guy1[idx] == str(num) :
            guy1_correct += 1
        if guy2[idx] == str(num) :
            guy2_correct += 1
        if guy3[idx] == str(num) :
            guy3_correct += 1
    
    correct_array = (guy1_correct, guy2_correct, guy3_correct)
    max_correct = max(correct_array)
    
    if guy1_correct == max_correct :
        answer.append(1)
    if guy2_correct == max_correct :
        answer.append(2)
    if guy3_correct == max_correct :
        answer.append(3)
    
    return answer
