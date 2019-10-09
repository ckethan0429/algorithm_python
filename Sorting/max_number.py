import itertools

def solution(numbers):
    # 자리수 일의자리, 십의자리, 백의자리, 1000까지 올수있음.
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))


    

print(solution([3,30,34,5,9]))