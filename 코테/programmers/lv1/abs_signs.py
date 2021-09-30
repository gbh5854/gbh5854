def solution(absolutes, signs):
    answer = []

    for i in range(len(absolutes)):
        if signs[i] == True:
            answer.append(absolutes[i])
        else:
            answer.append(absolutes[i]*-1)

    return sum(answer)


print(solution([4,7,12], [True,False,True]))

print(solution([1,2,3], [False,False,True]))