def solution(tickets):
    answer = []
    bfs = []
    visited = [0 for i in range(len(tickets))]
    
    tickets = sorted(tickets)    
    answer.append('ICN')    
    bfs.append([answer, visited])
    # print(tickets)
    
    while True:
        tmp = bfs.pop(0)
        # print("tmp = ", tmp)
        if 0 not in tmp[1]:
            answer = tmp[0]
            break
        
        target = tmp[0][-1]
        size = len(tickets)
        for idx in range(size):
            start = tmp[0][:]
            visit = tmp[1][:]
            # print(start, visit, bfs)
            if tickets[idx][0] == target and visit[idx] == 0:
                start.append(tickets[idx][1])
                visit[idx]+=1
                bfs.append([start, visit])

    return answer




# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]))