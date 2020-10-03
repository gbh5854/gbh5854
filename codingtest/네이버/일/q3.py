info = {}
depth_info = {}
tmp = {}
comb = []
ans_min = 9999999

def getDepth(node):
    return depth_info[node]

def dfs(depth, node):
    global depth_info
    for i in range(len(info[node])):
        # print(node, info[node][i])
        depth_info[info[node][i]] = depth + 1
        # if info[node][i] not in depth_info:
        #     depth_info = []
        if info[node][i] in info:
            dfs(depth + 1, info[node][i])

def cal_virus(comb):
    queue = []
    queue.append(0)
    result = 0
    while(len(queue) != 0):
        result += 1
        pop = queue[0]
        queue.remove(pop)
        # print(comb, info[queue[0]])
        if pop in info:
            for node in info[pop]:
                if node not in comb:
                    queue.append(node)
    # print("comb : ", comb, "result = ", result)
        
    return result

def solve(depth):
    global comb, ans_min
    if depth > len(tmp):
        # print(comb)
        res = cal_virus(comb)
        if res < ans_min:
            ans_min = res
    else:
        for node in tmp[depth]:
            comb.append(node)
            solve(depth+1)
            comb.remove(node)
            

def initialize(edges):
    global info, tmp
    for x,y in edges:
        if x not in info:
            info[x] = []
        info[x].append(y)

    dfs(0,0)
    for i in depth_info:
        if depth_info[i] not in tmp:
            tmp[depth_info[i]] = []
        tmp[depth_info[i]].append(i)

    solve(1)


def solution(n, edges):
    answer = 0

    initialize(edges)
    # print(info)
    # print(depth_info)
    # print(tmp)

    answer = ans_min
    return answer



# print(solution(19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))

# print(solution(14, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]]))

# print(solution(10, [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9]]))