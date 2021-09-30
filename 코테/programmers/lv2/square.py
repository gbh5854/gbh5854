import math

def solution(w,h):
    answer = 0

    if w == h:
        return w*h-w

    if w < h:
        for i in range(w):
            start_h = float(h)*i/float(w)
            end_h = float(h)*(i+1)/float(w)

            # print(start_h, end_h)
            answer += math.ceil(end_h) - math.trunc(start_h)
    else:
        for i in range(h):
            start_w = float(w)*i/float(h)
            end_w = float(w)*(i+1)/float(h)

            # print(start_h, end_h)
            answer += math.ceil(end_w) - math.trunc(start_w)        


    return w*h-answer



print(solution(8,12))

print(solution(4,4))