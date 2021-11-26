import sys
answer = 4000000

input1 = input()
input1 = input1.split(" ")
N = int(input1[0])
K = int(input1[1])
# print(N,K)
# map = [[0 for _ in range(2001)] for __ in range(2001)]
info = {}

def calculate(color):
    global answer
    # print(color)
    minx, maxx, miny, maxy = 1001, -1001, 1001, -1001
    for idx in range(len(color)):
        tmp = color[idx]
        x = tmp[0]
        y = tmp[1]

        if minx > x:    minx = x
        if maxx < x:    maxx = x
        if miny > y:    miny = y
        if maxy < y:    maxy = y
    res = (maxx-minx) * (maxy-miny)
    # print("area size : ", res)
    if res < answer:
        answer = res

def dfs(idx, color):
    global answer
    if idx > K:
        calculate(color)
        # print(color)
        return
    else:
        for i in range(len(info[idx])):
            color.append(info[idx][i])
            dfs(idx+1, color)
            color.pop()

# print(map)

for i in range(N):
    tmp = input()
    tmp = tmp.split(" ")
    x = int(tmp[0])
    y = int(tmp[1])
    color = int(tmp[2])
    # map[x][y] = color
    
    if color not in info:
        info[color] = []

    info[color].append([x,y])
# print(info)
color = []

dfs(1, color)

print(answer)
