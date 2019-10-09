def solution(array, commands):

    answer = []
    print(array)
    print()
    for i in range(len(commands)):
        array1 = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(array1[commands[i][2]-1])
        print(array1)
        
    return answer


print(solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]]))