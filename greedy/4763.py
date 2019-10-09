m_num = int(input())

rival = []
rival_num = []
rival_rel = []
for num in range(m_num):
    rival = input().split()
    rival_num.append(int(rival[0]))
    
    rrival = []
    for r in rival[1:]:
        r = int(r)
        rrival.append(r)
    rival_rel.append(rrival)


print(rival_num) # 앙숙관계 갯수
print(rival_rel) # 특정 앙숙관계 

# 
A = []
B = []
for num in range(1, m_num+1):
    if rival_num[num] == 1:
        A.append(num)
        continue
    elif rival_num[num] == 2:
        A.append(num)
        A.append(rival_rel[0])
        B.append(rival_rel[1])
        
