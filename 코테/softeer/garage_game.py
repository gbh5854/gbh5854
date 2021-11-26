import sys
import copy

N = int(input())
map = [[-1 for i in range(N)] for j in range(3*N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 0

def print_map():
    for i in range(3*N):
        print(map[i])
    print()

def print_garage():
    for i in range(2*N, 3*N):
        print(map[i])
    print()

def update_map():
    global map
    for y in range(N):
        cnt = 0
        for x in range(2*N, 3*N):
            if map[x][y] == 0:
                cnt+=1
            else:
                x-=1
                break
        if x == 3*N:
            x-=1

        while x >= cnt:
            map[x][y] = map[x-cnt][y]
            map[x-cnt][y] = 0
            x-=1


def calculate(x,y, visit):
    global map
    queue = []
    target = map[x][y]
    cnt = 1
    minx, maxx, miny, maxy = x,x,y,y
    queue.append([x,y])
    map[x][y] = 0
    while(len(queue) != 0):
        tmp = queue.pop(-1)
        # print(tmp)
        map[tmp[0]][tmp[1]] = 0
        for i in range(4):
            n_x = tmp[0] + dx[i]
            n_y = tmp[1] + dy[i]

            if n_x >= 2*N and n_x < 3*N and n_y >= 0 and n_y < N:
                if visit[n_x][n_y] == 0 and map[n_x][n_y] == target:
                    queue.append([n_x, n_y])
                    visit[n_x][n_y] = 1
                    map[n_x][n_y] = 0
                    cnt+=1
                    if n_x < minx:  minx = n_x
                    if n_x > maxx:  maxx = n_x
                    if n_y < miny:  miny = n_y
                    if n_y > maxy:  maxy = n_y
    result = cnt + ((maxx-minx+1) * (maxy-miny+1))
    return result




def dfs(idx,sum):
    global answer, map
    # print("idx = ",idx)
    # print_map()
    if idx == 3:
        if sum > answer:
            # print(sum)
            answer = sum
            return
    else:
        visit = [[0 for i in range(N)] for j in range(3*N)]
        temp_map = copy.deepcopy(map)

        for i in range(2*N, 3*N):
            for j in range(N):
                if visit[i][j] == 0:
                    visit[i][j] = 1
                    result= calculate(i,j, visit)
                    result += sum
                    update_map()
                    dfs(idx+1, result)
                    map = copy.deepcopy(temp_map)

for i in range(N*3):
    temp = input()
    temp = temp.split(" ")
    for j in range(len(temp)):
        map[i][j] = int(temp[j])
dfs(0,0)
print(answer)

