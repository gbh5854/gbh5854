# def comparator(a,b):
#     t1 = a+b
#     t2 = b+a
#     return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

# def solution(numbers):
#     answer = []
#     n = [str(x) for x in numbers]
#     # n = sorted(n, key=comparator,reverse=True)
#     n = list(map(comparator, n))
#     print(n)
#     # answer = str(int(''.join(n)))
#     return answer

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)   #*3하는 이유 = 자리수 채우기 위해

    return str(int(''.join(numbers)))


# print(solution([6, 10, 2]))

print(solution([3, 30, 34, 5, 9]))

print(solution([1000, 0, 5, 99, 100]))

# print(solution([979, 97, 998, 993, 9]))