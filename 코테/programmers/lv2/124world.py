def solution(n):
    answer = ''
    idx = 1
    
    #3진수 표현 (0,1,2만 사용) -> 0->1 1->2 2->4
    #10 = 

    cnt = 0
    while cnt < n:
        cnt += 3**idx
        idx+=1
    print(cnt, idx)
    
    print(n)
    for i in range(1,idx):
        tmp = int(n % 3)
        print(n, tmp)
        n-=tmp 
    return answer


# print(solution(1))

# print(solution(2))

print(solution(13))

print(solution(11))