visit = []

def dfs(idx, computers):
    global visit
    if idx in visit:
        visit.remove(idx)
    for i in range(len(computers)):
        # print(computers[idx][i])
        if computers[idx][i] == 1 and i in visit:
            dfs(i, computers)
        

def solution(n, computers):
    global visit
    i = 1
    answer = 0
    visit = []
    
    for i in range(n):
        visit.append(i)
    while len(visit) != 0:
        dfs(visit[0], computers)
        answer+=1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))