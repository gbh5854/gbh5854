def solution(answers):
    answer = []
    answer2 = []
    max_cnt = 0
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    idx_p1 = idx_p2 = idx_p3 = 0
    cnt_p1 = cnt_p2 = cnt_p3 = 0
    
    for idx in range(len(answers)):
        if p1[idx_p1] == answers[idx]:
            cnt_p1+=1
        if p2[idx_p2] == answers[idx]:
            cnt_p2+=1
        if p3[idx_p3] == answers[idx]:
            cnt_p3+=1
            
        if idx_p1 == len(p1)-1:
            idx_p1 = 0
        else:
            idx_p1+=1 
        if idx_p2 == len(p2)-1:
            idx_p2 = 0
        else:
            idx_p2+=1 
        if idx_p3 == len(p3)-1:
            idx_p3 = 0
        else:
            idx_p3+=1    
   
    # print(cnt_p1, cnt_p2, cnt_p3)
    answer2.append(cnt_p1)
    answer2.append(cnt_p2)
    answer2.append(cnt_p3)
    
    for i in answer2:
        if i > max_cnt:
            max_cnt = i

    for i in range(len(answer2)):
        if max_cnt == answer2[i]:
            answer.append(i+1)
        
    return answer

print(solution([1,2,3,4,5]))

print(solution([1,3,2,4,2]))

print(solution([1,3,2,4,2,4,1,5,2,3,2,3,4,1]))