pasta_list = []
ade_list = []
#pasta입력받기
for num in range(0,3):
    pasta = int(input())
    pasta_list.append(pasta)

#ade입력받기
for num in range(0,2):
    ade = int(input())
    ade_list.append(ade)

pasta_min = pasta_list[0]
for pasta in pasta_list:
    if pasta < pasta_min :
        pasta_min = pasta
    
ade_min = ade_list[0]
for ade in ade_list:
    if ade < ade_min :
        ade_min = ade

price = (pasta_min + ade_min ) * 1.1
print('{0:0.1f}'.format(price))

