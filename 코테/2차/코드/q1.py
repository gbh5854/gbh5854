

def check_program(string, program):
    if string.split(" ")[0] == program: 
        return True
    else:
        return False

def solution(program, flag_rules, commands):
    answer = []
    flag_info = {}

    for command in commands:
        if not check_program(command, program):     #cmd error
            answer.append(False)
        else:
            idx = 1
            cmd_list = []
            ans_flag = True

            for flag in flag_rules:
                split_flag = flag.split(" ")

                if split_flag[1] == "STRING":
                    flag_info[split_flag[0]] = 1
                elif split_flag[1] == "NUMBER":
                    flag_info[split_flag[0]] = 2
                elif split_flag[1] == "NULL":
                    flag_info[split_flag[0]] = 3
            # print(flag_info)

            token = command.split(" ")
           
            # print(token)
            while(idx < len(token)):
                if token[idx] in flag_info:
                    if flag_info[token[idx]] == 1 or flag_info[token[idx]] == 2:
                        cmd_list.append([token[idx], token[idx+1]])
                        idx+=2
                    else:
                        cmd_list.append([token[idx]])
                        idx+=1
                else:
                    ans_flag = False
                    break
            
            # print(cmd_list)
            if ans_flag == True:
                for cmd in cmd_list:
                    if flag_info[cmd[0]] == 1:      #STRING
                        if len(cmd) == 2:
                            if cmd[1].isalpha():
                                continue
                            else:
                                ans_flag = False
                                break
                        else:
                            ans_flag = False
                            break
                    elif flag_info[cmd[0]] == 2:    #NUMBER
                        if len(cmd) == 2:
                            if cmd[1].isdigit():
                                continue
                            else:
                                ans_flag = False
                                break
                        else:
                            ans_flag = False
                            break
                    elif flag_info[cmd[0]] == 3:    #NULL
                        if len(cmd) == 1:
                            continue
                        else:
                            ans_flag = False
                            break

            answer.append(ans_flag)
    return answer


print(solution(
    "line",
    ["-s STRING", "-n NUMBER", "-e NULL"],
    ["line -n 100 -s hi -e", "lien -s Bye"]
))

print(solution(
    "line",
    ["-s STRING", "-n NUMBER", "-e NULL"],
    ["line -s 123 -n HI", "line fun"]
))
