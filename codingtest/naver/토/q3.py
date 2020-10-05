from itertools import combinations
from itertools import permutations
from math import comb

make = [6,2,5,5,4,5,6,3,7,6]
sort_num = [1,7,4,2,3,5,0,6,9,8]
tmp = []
tmp2 = []
res = 0

def cal_ncr2(dic, size):
    n_size = size
    ans = 1
    for i in dic:
        ans *= comb(n_size, dic[i])
        n_size -= dic[i]        
    return ans

def cal_ncr(num):
    temp = {}
    num_size = len(str(num))
    ans = 1
    for i in sorted(str(num)):
        if i not in temp:
            temp[i] = 0
        temp[i] += 1
    if '0' not in str(num):
        # print(temp)
        # print(len(temp))
        for i in temp:
            # print(num_size, "C", temp[i])
            ans *= comb(num_size, temp[i])
            num_size -= temp[i]
        # print("ans = ", ans)
    else:
        ans = 0
        # print(temp)
        for i in temp:
            if i != '0':
                temp[i] -=1
                # print(temp)
                ans += cal_ncr2(temp, num_size-1)
                temp[i] +=1
            

    # print(num, ans)
    return ans


def dfs(n, k, num, index):
    global res
    # print(num)
    if n == k:
        # print(num)
        if sorted(str(num)) not in tmp2:
            tmp2.append(sorted(str(num)))
            # tmp.append(num)
            res+=cal_ncr(num)       
        return
    else:
        # for i in range(10):
        #     if n + make[i] <= k:
        #         if i == 0 and index == 0:
        #             continue
        #         else:
        #             dfs(n + make[i], k, num*10 + i, index + 1)
        for i in sort_num:
            # print(num, int(str(num)[-1]))

            if int(str(num)[-1]) <= i or i == 0:
                if n + make[i] <= k:
                    if i == 0 and index == 0:
                        continue
                    else:
                        dfs(n + make[i], k, num*10 + i, index + 1)
                        if i == 6 and index != 0:
                            dfs(n + make[i], k, num*10 + 0, index)
                else:
                    return


def solution(k):
    global res
    answer = 0
    if k < 3:
        return 0
    if k == 6:
        tmp.append(0)
        res+=1
    dfs(0,k,0, 0)
    # print(len(tmp))
    # print(tmp)
    # print(tmp2)

    # answer = len(tmp)
    # for i in tmp:
    #     answer += cal_ncr(i)
    answer = res
    return answer

    # tmp = []
    # a = "100"
    # b = "14121"
    # # print(a[-1])
    # a = sorted(a)
    # tmp.append(a)
    # b = sorted(b)
    # # if b in tmp:
    # #     print(1)
    # # print(int(a))
    # t = set(list(permutations(a)))
    # zzz = 0
    # for i in t:
    #     if i[0] != '0':
    #         zzz+=1
    # print(len(set(list(permutations(a)))))
    # print(zzz)

print(solution(34))
