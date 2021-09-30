def solution(new_id):
    answer = ''
    char = ['-', '_', '.']
    
    answer = "".join(c for c in new_id.lower() if c.isalnum() or c in char)

    if len(answer) != 0:
        cnt = 0
        idx = 0
        while idx < len(answer)-1:
            if answer[idx] == '.' and answer[idx+1] == '.':
                answer = answer[:idx] + answer[idx+1:]
            else:
                idx+=1

    while len(answer) != 0 and answer[0] == '.':
        if len(answer) == 1:
            answer = ''
            break
        else:
            answer = answer[1:]

    while len(answer) != 0 and answer[-1] == '.':
        if len(answer) == 1:
            answer = ''
            break
        else:
            answer = answer[:-1]

    if len(answer) == 0:
        answer+='a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2:
        answer = answer + answer[-1]*3
        answer = answer[:3]
        
    return answer

#남의 풀이 - 정규식 사용
# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st

print(solution("...!@BaT#*..y.\\\\\\abcdefghijklm."))

print(solution("z-+.^."))

print(solution("=.="))

print(solution("123_.def"))

print(solution("abcdefghijklmn.p"))