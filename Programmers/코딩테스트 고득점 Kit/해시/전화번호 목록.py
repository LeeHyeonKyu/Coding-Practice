def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x : -len(x))
    
    while phone_book :
        checker = phone_book.pop()
        for num in phone_book :
            if num.startswith(checker) :
                return False
            
    return True
