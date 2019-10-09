def solution(answers):
# 문제1 : 찍는 패턴개수와 문제수가 다르다.
# 1, 2, 3, 4, 5, 1, 2, 3, 4, 5
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# 문제2 : 각각 맞춘 개수를 찾았지만, 당사자를 찾아야한다
#  
    
    test1 = [1,2,3,4,5]
    test2 = [2,1,2,3,2,4,2,5]
    test3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num = len(answers)
    one = []
    two = []
    three = []
    result= []
    for i in range(num):
        one.append(test1[i%5])
        two.append(test2[i%8])
        three.append(test3[i%10])

    
    count = [0,0,0]
    for i in range(0, len(answers)):
        
        if answers[i] == one[i]:
            count[0] += 1
        if answers[i] == two[i]:
            count[1] += 1
        if answers[i] == three[i]:
            count[2] += 1
    
    for idx, c in enumerate(count):
        if c == max(count):
            result.append(idx+1)
    return result
        

print(solution([1,2,3,4,5]))