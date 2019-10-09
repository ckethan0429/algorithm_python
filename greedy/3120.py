now, hope = input().split()
now = int(now)
hope = int(hope)
gap = abs(now-hope)
#print(gap)

count = 0

while(gap >= 10):
    count += 1
    gap -= 10


if (gap == 9):
    count += 2
elif gap == 8 :
    count += 3

elif gap == 7 :
    count += 3

elif gap == 6 :
    count += 2

elif gap == 5 :
    count += 1

elif gap == 4 :
    count += 2

elif gap == 3 :
    count += 3

elif gap == 2 :
    count += 2

elif gap == 1 :
    count += 1

print(count)

