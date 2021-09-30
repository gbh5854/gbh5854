import math

def find_sol(x,y):
    cnt_b = 0
    # print("x,y = ",x,y)
    for i in range(x):
        # print("i = ", i)
        if i == 1 or i == x-1:
           cnt_b += y
        else:
            if y == 1:
                cnt_b+=1
            else:
                cnt_b+=2
    return (cnt_b, (x*y)-cnt_b)
    
def solution(brown, yellow):
    answer = []
    
    total_cnt = brown+yellow
    
    # print(total_cnt)
    for i in range(1,int(math.sqrt(total_cnt))+1 ):
        # print(i)
        if total_cnt % i == 0:
            if find_sol(i, int(total_cnt/i)) == (brown, yellow):
                answer.append(int(total_cnt/i))
                answer.append(i)
                break
                
    return answer

#다른사람 풀이
#공식활용
#둘레 = 2(x+y)-4
#내부 = (x-2)(y-2)
# def solution(brown, red):
#     for i in range(1, int(red**(1/2))+1):
#         if red % i == 0:
#             if 2*(i + red//i) == brown-4:
#                 return [red//i+2, i+2]

print(solution(10,2))

print(solution(8,1))

print(solution(24,24))