arr = [[] for row in range(9)]
arr_cal = []

def dfs(N, idx, target):
    global arr, arr_cal

    if target == 1:
        # arr[1].append(N)
        return
    else:
        if idx == target-1:
            print(arr_cal)
        else:
            for j in range(5):
                arr_cal.append(j)
                dfs(N, idx+1, target)
                del arr_cal[len(arr_cal)-1]


def print_arr(arr):
    for i in arr:
        for j in i:
            print(j, end = "\t")
        print()

def solution(N, number):
    global arr_cal
    answer = 0

    for idx in range(1,4):
        print(idx)
        dfs(N, 0, idx)
        print_arr(arr)


    return answer




print(solution(5,12))

# print(solution(2,11))