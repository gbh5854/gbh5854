def solution(record):
    answer = []
    tmp = []
    id_list = {}

    for i in record:
        temp = list(i.split(" "))
        tmp.append(temp)

        if len(temp) == 3:
            tmp_id, tmp_name = temp[1], temp[2]
            if temp[0] == "Enter" or temp[0] == "Change":
                id_list[tmp_id] = tmp_name

    for i in range(len(tmp)):
        if tmp[i][0] == "Enter":
            answer.append(id_list[tmp[i][1]]+"님이 들어왔습니다.")
        elif tmp[i][0] == "Leave":
            answer.append(id_list[tmp[i][1]]+"님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", 
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))

