# 내꺼
def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(1, len(phone_book)):
        length = len(phone_book[i-1])
        
        if phone_book[i-1] == phone_book[i][:length]:
            answer = False
            
    return answer

# 다른사람들꺼
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#     print(phoneBook)
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         print(p1, p2)
        
#     print()
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         print(p1,p2)
#         if p2.startswith(p1):
#             return False
#     return True

# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer


print(solution(["119", "97674223", "1195524421"]))

print(solution(["123","456","789"]))

print(solution(["12","123","1235","567","88"]))