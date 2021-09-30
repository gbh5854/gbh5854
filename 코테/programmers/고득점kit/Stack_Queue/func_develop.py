# def solution(progresses, speeds):
#     answer = []
#     work = []
    
#     for i in range(len(progresses)):
#         rest = 100 - progresses[i]
#         if rest % speeds[i] == 0:
#             work.append(rest/speeds[i])
#         else:
#             work.append(int(rest/speeds[i])+1)
    
#     idx = 1
#     cnt = 1
#     tmp = work[0]
    
#     while idx <= len(work):
#         if idx >= len(work):
#             answer.append(cnt)
#             break
#         else:
#             if tmp >= work[idx]:
#                 cnt+=1
#             else:
#                 answer.append(cnt)
#                 cnt = 1
#                 tmp = work[idx]
#             idx+=1   

#     return answer

#다른사람 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
        print(Q)
    return [q[1] for q in Q]


print(solution([93, 30, 55], [1, 30, 5]))

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
