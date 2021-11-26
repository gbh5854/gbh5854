import sys
from itertools import permutations

answer = 9999999
input1 = input()
input1 = input1.split(" ")
N = int(input1[0])
M = int(input1[1])
K = int(input1[2])

# print(N,M,K)

input2 = input()
input2 = input2.split(" ")
weight_list = []

for i in range(len(input2)):
    weight_list.append(int(input2[i]))
# print(weight_list)

p_list = list(permutations(weight_list, N))

for idx in range(len(p_list)):
    case = p_list[idx]
    sum = 0
    res = 0
    cnt = 0
    index = 0

    while cnt < K:
        if sum+case[index%N] <= M:
            sum+=case[index%N]
            index+=1
        else:
            cnt+=1
            res+=sum
            sum = 0
        
        if cnt == K:
            break
    # print(res)
    if answer > res:
        answer = res

print(answer)
