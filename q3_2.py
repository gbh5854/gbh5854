from itertools import combinations
from itertools import permutations
from math import comb

# make = [6,2,5,5,4,5,6,3,7,6]
# sort_num = [1,7,4,2,3,5,0,6,9,8]

res = 0
f = [0,0,1,1,1,3,3,1]       ##f(x) return value list
tmp = {}

def cal_ncr2(dic, size):
    n_size = size
    ans = 1
    for i in dic:
        ans *= comb(n_size, dic[i])
        n_size -= dic[i]        
    return ans

# def cal_ncr(num):
#     temp = {}
#     num_size = len(str(num))
#     ans = 1
#     for i in sorted(str(num)):
#         if i not in temp:
#             temp[i] = 0
#         temp[i] += 1
#     if '0' not in str(num):
#         # print(temp)
#         # print(len(temp))
#         for i in temp:
#             # print(num_size, "C", temp[i])
#             ans *= comb(num_size, temp[i])
#             num_size -= temp[i]
#         # print("ans = ", ans)
#     else:
#         ans = 0
#         # print(temp)
#         for i in temp:
#             if i != '0':
#                 temp[i] -=1
#                 # print(temp)
#                 ans += cal_ncr2(temp, num_size-1)
#                 temp[i] +=1
            

#     print(num, ans)
#     return ans

def calculate(tmp,k):
    result = 0
    ans = 1
    ans1 = 0
    ans2 = 0
    size = 0
    for i in tmp:
        size += tmp[i]
    tmp_size = size
    # print(tmp, size)

    for i in tmp:
        # print(size, "C", tmp[i])
        ans *= comb(tmp_size, tmp[i])
        tmp_size -= tmp[i]
    
    # # t = list(permutations(tmp))
    # # print(t)
    # print("ans = ", ans)
    if 6 in tmp:
        tmp[6]-=1
        ans2 = cal_ncr2(tmp, size-1)
        ans1 = ans - ans2
        tmp[6]+=1
    else:
        ans1 = ans
    # print("ans1 = ", ans1, ", ans2 = ", ans2)

    # print(tmp)
    temp = 1
    for j in tmp:
        if tmp[j] != 0:
            for l in range(tmp[j]):
                temp *= f[j]

    for i in range(ans1): ## 0 not first
        result += temp

    # print("result = ", result)

    if 6 in tmp:
        if k == 6:
            result += 3
        else:
            flag = True
            # tmp[6]-=1
            temp = 1
            for j in tmp:
                if j == 6:
                    for l in range(tmp[j]):
                        if flag == True:
                            temp *= f[j]-1
                            flag = False
                        else:
                            temp *= f[j]
                else:
                    for l in range(tmp[j]):
                        temp *= f[j]


            for i in range(ans2): ## 0 first
                result += temp            
                    
    # print("result = ", result, "\n")
        # for j in tmp:



    return result



def dfs(n,k):
    global tmp, res
    if n == k:
        # print(tmp)
        res += calculate(tmp,k)
    
    else:
        for i in range(2,8):
            if n + i <= k:
                flag = True
                for j in tmp:
                    if i < j:
                        flag = False
                        break
                
                if flag == True:
                    if i not in tmp:
                        tmp[i] = 0
                    tmp[i]+=1
                    dfs(n + i, k)
                    tmp[i]-=1
                    if tmp[i] == 0:
                        del(tmp[i])


def solution(k):
    global res
    answer = 0
    if k < 2:
        return 0

    dfs(0,k)

    return res


print(solution(46))