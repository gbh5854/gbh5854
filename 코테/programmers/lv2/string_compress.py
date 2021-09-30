def solution(s):
    answer = 0
    idx = 0
    ss = []

    for i in range(1, int(len(s) / 2) + 1): #절반까지 계산
        idx = 0
        cnt = 1
        target = s[idx:idx+i]
        string = ''

        while idx < len(s):
            target2 = s[idx+i:idx+(i*2)]
            if target == target2:
                cnt+=1
                idx+=i
            else:
                if cnt != 1:
                    string=string+str(cnt)+target
                else:
                    string+=target
                idx+=i
                target = s[idx:idx+i]
                cnt = 1
        if string!= "":
            ss.append(len(string))

    if len(ss) == 0:
        return len(s)
    else:
        return min(ss)


print(solution("ababcdedededededededededede"))

print(solution("acacacacacacbacacacacacac"))

print(solution("aabbaccc"))

print(solution("ababcdcdababcdcd"))

print(solution("abcabcdede"))

print(solution("abcabcabcabcdededededede"))

print(solution("xababcdcdababcdcd"))