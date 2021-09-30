visit = []
answer = 100
tmp_list = []

def dfs(begin, target, words, cnt):
    global answer
    
    if begin == target:
        # print("cnt = ", cnt, tmp_list)
        if answer > cnt:
            answer = cnt
        return
    
    for idx in range(len(words)):
        tmp = words[idx]
        change = 0
        for i in range(len(tmp)):
            if begin[i] != tmp[i]:
                change+=1
            if change > 1:
                break
        if change == 1 and visit[idx] == 0:
            visit[idx] = 1
            tmp_list.append(tmp)
            dfs(tmp, target, words, cnt+1)
            visit[idx] = 0
            tmp_list.remove(tmp)

def solution(begin, target, words):
    global visit, answer
    answer = 100
    visit = [0 for i in range(len(words))]
    
    if target not in words:
        return 0
    
    dfs(begin, target, words, 0)
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))