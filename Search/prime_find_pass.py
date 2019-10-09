import itertools

def solution(numbers):
    # 문자열로 입력이 들어왔을 때 리스트로 변환해주면 각 요소들이 들어온다.
    # 011
    print(numbers)
    number = list(numbers)
    # ['0', '1', '1']
    print(number)
    print()
    print()
    a = []
    for i in range(1, len(numbers)+1):
        a += list(map(''.join, itertools.permutations(number,i)))
        print(a)
    
    # ['0', '1', '1', '01', '01', '10', '11', '10', '11', '011', '011', '101', '110', '101', '110']
    # set을 통하여 중복요소 제거
    a = list(set(map(int,a)))
    
    #[0, 1, 101, 10, 11, 110]
    print(a)

    # [0, 1, 10, 11, 101, 110]
    a.sort()
    print(a)

    answer = 0
    for i in a:
        if i < 2:
            pass
        elif i == 2:
            answer += 1
        else:
            for j in range(2, i):
                if i % j == 0:
                    break
                elif j== i-1:
                    answer += 1
    return answer

print(solution("011"))