import itertools
import math 

def isPrime(number):
    end = int(math.sqrt(number))
    for i in range(2, end):
        if number % i == 0:
            return False
    return True
        
def solution(numbers):
    answer = 0
    
    result = []
    for i in numbers:
        result.append(i)
    
    
    for number in itertools.permutations(numbers):
        sum = ''
        for n in number: 
            sum += n
        result.append(sum)
    
    result = set(map(int, result))
    print(result)
    #print(int(set(result))
    for r in result:
        print('{}일때'.format(r))
        if r!= 0 and r != 1 and isPrime(r) == True:
            answer += 1
            
       
    print(answer)
    return answer