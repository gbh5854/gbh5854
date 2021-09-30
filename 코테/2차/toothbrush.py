import math

answer = []
tree_info = []
account = {}
parent_list = {}

def cal_money(tree_info, node_name, money):
    global answer
    # print(tree_info[node_idx])
    # print(money - math.trunc(money*0.1), math.trunc(money*0.1))
    idx = account[node_name]
    
    if math.trunc(money*0.1) == 0:
        answer[idx]+=money
        return
    else:
        answer[idx]+=money - math.trunc(money*0.1)
        parent = tree_info[idx][2]
        if tree_info[idx][2] == "-":
            return
        else:
            cal_money(tree_info, parent, math.trunc(money*0.1))

def solution(enroll, referral, seller, amount):
    global answer
    global tree_info
    global account
    global parent_list

    answer = []
    tree_info = []
    account = {}
    parent_list = {}

    for i in range(len(enroll)):
        answer.append(0)
        account[enroll[i]] = 0

    for idx in range(len(enroll)):
        tree_info.append([idx, enroll[idx], referral[idx]])
        account[enroll[idx]] = idx

    for node_idx in range(len(enroll)):
        parent_list[enroll[node_idx]] = referral[node_idx]

    for sell in range(len(seller)):
        cal_money(tree_info, seller[sell], amount[sell]*100)

    return answer



print(solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]
))

print(solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["sam", "emily", "jaimie", "edward"],
    [2, 3, 5, 4]
))