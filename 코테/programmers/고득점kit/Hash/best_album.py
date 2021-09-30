def solution(genres, plays):
    answer = []
    playlist = {}
    playlist2 = {}
    
    for idx in range(len(genres)):
        if genres[idx] not in playlist:
            playlist[genres[idx]] = 0
        playlist[genres[idx]] += plays[idx]
        
    for idx in range(len(genres)):
        if genres[idx] not in playlist2:
            playlist2[genres[idx]] = []
        playlist2[genres[idx]].append([plays[idx], idx])
        
    # print(playlist)
    # print(playlist2)
    # print(playlist)
    a = sorted(playlist.items(), key=lambda x: x[1], reverse=True)
    # print(a)
    
    for i in a:
        genre = i[0]
        # print(playlist2[genre])
        
        b = sorted(playlist2[genre], key=lambda x : x[0], reverse=True)
        # print(b)
        
        if len(b) >= 2:
            for idx in range(2):
                answer.append(b[idx][1])
        else:
            answer.append(b[0][1])
        
    return answer




print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))


print(solution(["classic", "pop", "classic", "classic", "classic", "classic"], 
               [500, 1000, 400, 300, 200, 100]))