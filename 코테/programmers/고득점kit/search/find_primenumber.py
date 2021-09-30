import math

prime_list=[]
select = []

def find_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def sol(idx, value, num_list):
    global prime_list
    
    if idx == len(num_list):
        if value not in prime_list:
            prime_list.append(value)
        return
    for i in range(len(num_list)):
        if select[i] == 0:      
            tmp = value*10 + int(num_list[i])
            select[i] = 1
            sol(idx+1, tmp, num_list)
            select[i] = 0
            sol(idx+1, value, num_list)

def solution(numbers):
    global prime_list, select
    answer = 0
    prime_list = []
    num_list = list(numbers)
    for i in range(len(num_list)):
        select.append(0)
    # print(num_list)
    sol(0,0,num_list)
    # print(prime_list)
    for num in prime_list:
        if find_prime(num) == True:
            answer+=1
    return answer


print(solution("17"))

print(solution("011"))