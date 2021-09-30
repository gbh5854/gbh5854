

def check_program(string, program):
    if string.split(" ")[0] == program: 
        return True
    else:
        return False

def check_alpha(string):
    if string.isalpha():
        return True
    else:
        return False

def check_num(string):
    if string.isdigit():
        return True
    else:
        return False

def check_null(string):
    if len(string) == 1:
        return True
    else:
        return False

def solution(program, flag_rules, commands):
    answer = []

    for command in commands:
        flag_info = {}
        alias_info = []
        if not check_program(command, program):     #cmd error
            answer.append(False)
        else:
            idx = 1
            cmd_list = []
            ans_flag = True

            for flag in flag_rules:
                split_flag = flag.split(" ")

                if len(split_flag) == 2:
                    if split_flag[1] == "STRING":
                        flag_info[split_flag[0]] = 1
                    elif split_flag[1] == "NUMBER":
                        flag_info[split_flag[0]] = 2
                    elif split_flag[1] == "NULL":
                        flag_info[split_flag[0]] = 3
                    elif split_flag[1] == "STRINGS":
                        flag_info[split_flag[0]] = 4
                    elif split_flag[1] == "NUMBERS":
                        flag_info[split_flag[0]] = 5 
                elif len(split_flag) == 3:
                    alias_info.append([split_flag[0], split_flag[2]])


            print(alias_info)
            print(flag_info)

            token = command.split(" ")
           
            # print(token)
            while(idx < len(token)):
                if token[idx] in flag_info:
                    if flag_info[token[idx]] != 3:
                        tmp_list = []
                        tmp_idx = idx+1
                        
                        while(tmp_idx < len(token)):
                            if "-" not in token[tmp_idx]:
                                tmp_list.append(token[tmp_idx])
                                tmp_idx+=1
                            else:
                                break

                        cmd_list.append([token[idx], tmp_list])
                        idx = tmp_idx
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
                        # print(cmd[1], len(cmd[1]))
                        if len(cmd) == 2:
                            if len(cmd[1]) == 1:
                                if cmd[1][0].isalpha():
                                    continue
                                else:
                                    ans_flag = False
                                    break
                            else:
                                ans_flag = False
                                break
                        else:
                            ans_flag = False
                            break

                    elif flag_info[cmd[0]] == 2:    #NUMBER
                        if len(cmd) == 2:
                            if len(cmd[1]) == 1:
                                if cmd[1][0].isdigit():
                                    continue
                                else:
                                    ans_flag = False
                                    break
                            else:
                                ans_flag = False
                                break
                        else:
                            ans_flag = False
                            break
                    elif flag_info[cmd[0]] == 3:    #NULL
                        if check_null(cmd):
                            continue
                        else:
                            ans_flag = False
                            break
                    elif flag_info[cmd[0]] == 4:    #STRINGS
                        for i in cmd[1]:
                            if not check_alpha(i):
                                ans_flag = False
                                break
                    elif flag_info[cmd[0]] == 5:    #NUMBERS
                        for i in cmd[1]:
                            if not check_num(i):
                                ans_flag = False
                                break                    

            answer.append(ans_flag)
    return answer


print(solution(
    "line",
    ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"],
    ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]
))

print(solution(
    "bank",
    ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"],
    ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]
))
