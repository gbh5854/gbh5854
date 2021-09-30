def solution(board, moves):
    answer = 0
    doll_list = []

    for move in moves:
        for row in range(len(board)):
            if board[row][move-1] != 0:
                target = board[row][move-1]
                board[row][move-1] = 0

                if len(doll_list) != 0:
                    if doll_list[-1] == target:
                        doll_list.pop()
                        answer+=2
                    else:
                        doll_list.append(target)
                else:
                    doll_list.append(target)
                break

    return answer




print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
            , [1,5,3,5,1,2,1,4]))