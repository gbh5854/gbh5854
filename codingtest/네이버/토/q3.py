make = [6,2,5,5,4,5,6,3,7,6]
make = [1,7,2,3,5,]
tmp = []
def dfs(n, k, num, index):
    if n == k:
        tmp.append(num)
        return
    else:
        for i in range(10):
            if n + make[i] <= k:
                if i == 0 and index == 0:
                    continue
                else:
                    dfs(n + make[i], k, num*10 + i, index + 1)

                

def solution(k):
    answer = 0
    if k < 3:
        return 0
    if k == 6:
        tmp.append(0)
    dfs(0,k,0, 0)
    # print(tmp)

    answer = len(tmp)
    return answer


print(solution(30))
