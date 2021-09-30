answer = 0

def dfs(idx, value, numbers, target):
    global answer
    if idx == len(numbers):
        if value == target:
            answer+=1
        return
    dfs(idx+1, value+numbers[idx], numbers, target)
    dfs(idx+1, value-numbers[idx], numbers, target)

def solution(numbers, target):
    global answer
    answer = 0
    
    dfs(0,0,numbers,target)
    return answer

#다른사람 풀이
#Solution 함수 자체를 재귀로 돌려버림
#target == 0 인 이유 : numbers의 합이 target인 경우의 수 == -target인 경우의 수 (합이 -target이라고 생각한듯)
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
print(solution([1,1,1,1,1], 3))