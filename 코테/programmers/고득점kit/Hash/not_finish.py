def solution(participant, completion):
    answer = ''

    participant = sorted(participant)
    completion = sorted(completion)
    completion.append(1)
    
    for idx in range(len(completion)):
        if participant[idx] != completion[idx]:
            answer = participant[idx]
            break
    return answer







print(solution(["leo", "kiki", "eden"], 
                ["eden", "kiki"]))

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], 
                ["josipa", "filipa", "marina", "nikola"]))

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))