# tmp = []
# answer = 0

# def calculate(select, idx):
#     global tmp, answer
#     if idx == len(select):
#         # print(tmp)
#         result = 1
#         for i in range(len(select)):
#             if tmp[i] == 1:
#                 result *= select[i]
#         answer += result
#         # print("answer = ", answer, "result = ",result)
#         return
#     else:        
#         tmp[idx] = 1
#         calculate(select, idx+1)
#         tmp[idx] = 0
#         calculate(select, idx+1)                

def solution(clothes):
    # global tmp, answer
    tmp = []
    answer = 0
    clothes_list = {}
    select = []
    
    for cloth_name, close_class in clothes:
        if close_class not in clothes_list:
            clothes_list[close_class] = []
        clothes_list[close_class].append(cloth_name)        
    # print(clothes_list)
    
    for cloth in clothes_list:
        select.append(len(clothes_list[cloth]))
        tmp.append(0)     
       
    # print(select, tmp)
    
    if len(select) == 1:
        return len(clothes)
    else:
        # calculate(select, 0)
        answer = 1
        for num in select:
            answer = answer * (num+1)   
    
    return answer-1



print(solution([["yellowhat", "headgear"], 
                ["bluesunglasses", "eyewear"], 
                ["green_turban", "headgear"]]))


print(solution([["crowmask", "face"], 
                ["bluesunglasses", "face"], 
                ["smoky_makeup", "face"]]))