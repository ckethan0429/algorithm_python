n=100
# 0과 1은 False로 고정, 나머지는 True로 초기화
a = [False,False] + [True]*(n-1)
#print(a)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    print(primes)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)