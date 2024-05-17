def solution(phone_book):
    answer = True
    
#     phone_book.sort(key = lambda x: len(x))
    
#     for i in range(len(phone_book)):
#         for j in range(i+1, len(phone_book)):
#             if (phone_book[i] == phone_book[j][0:len(phone_book[i])]):
#                 return False

    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            return False
    
    return answer