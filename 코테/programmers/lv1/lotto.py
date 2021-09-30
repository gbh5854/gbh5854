def solution(lottos, win_nums):
    answer = []
    max_num = 0
    min_num = 0

    for num in lottos:
        if num == 0:
            max_num+=1
        elif num in win_nums:
            max_num+=1
            min_num+=1
        
    answer.append(7-max_num if max_num != 0 else 6)
    answer.append(7-min_num if min_num != 0 else 6)
        
    return answer



print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))

print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

print(solution([1,2,5,6,7,11], [20, 9, 3, 45, 4, 35]))