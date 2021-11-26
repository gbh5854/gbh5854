import sys

H, W = input().split(' ')
H = int(H)
W = int(W)
image_map = []
cmd_list = []
idx_x = [-1,1,0,0]
idx_y = [0,0,-1,1]

def print_map():
    for i in image_map:
        print(i)

def convert_color(dx,dy,color):
    target = image_map[dx][dy]
    queue = []
    queue.append([dx, dy])

    while(len(queue) != 0):
        i_x, i_y = queue.pop()

        for i in range(4):
            n_x = i_x + idx_x[i]
            n_y = i_y + idx_y[i]

            if n_x >= 0 and n_x < H and n_y >= 0 and n_y < W:
                if image_map[n_x][n_y] == target:
                    image_map[n_x][n_y] = color
                    queue.append([n_x, n_y])


for i in range(H):
    tmp = input().split(' ')
    tmp = list(map(int, tmp))
    image_map.append(tmp)

# for i in map:
#     print(i)

Q = input()
Q = int(Q)

# print("\n\n")
# print_map()
for i in range(Q):
    tmp = input().split(' ')
    cmd_list.append([int(tmp[0]), int(tmp[1]), int(tmp[2])])

for i in range(len(cmd_list)):
    # print(cmd_list[i])
    dx = cmd_list[i][0]-1
    dy = cmd_list[i][1]-1
    color = cmd_list[i][2]

    convert_color(dx,dy,color)

for i in range(H):
    for j in range(W):
        if j == W-1:
            print(image_map[i][j])
        else:
            print(image_map[i][j], end=' ')
