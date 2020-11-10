def solution(phone_book):
    
    answer = True
    phone_book.sort(reverse=True)

    for i in range(len(phone_book)) :
        finder = phone_book.pop()
        len_finder = len(str(finder))

        for num in phone_book :
            if str(num)[:len_finder] == str(finder) :
                answer = False
                break

        if answer == False :
            break

    return answer
