# 토핑개수 받기
topping_num =int(input())

#도우값, 토핑값
dough_price, topping_price = input().split()
dough_price = int(dough_price)
topping_price = int(topping_price)

#토핑 칼로리
topping_cal = []
for cal in range(topping_num):
    cal = int(input())
    topping_cal.append(cal)



total = 2 ** topping_num
print(bin(total))
wtf = []
for binary in range(total):
    print(bin(binary))
    wtf.append(bin(binary >> 2) + bin(binary >> 1) + bin(binary >> 0))