viloyat=['Toshkent','Xorazm','Andijon','Buxoro','Navoiy','Jizzax']

print(viloyat)                       #1

print(len(viloyat))                  #2

print(sorted(viloyat))               #3

print(sorted(viloyat,reverse=True))  #4

print(viloyat)                       #5

viloyat.sort()                       #6
print(viloyat)

sonlar=list(range(180,1800,2))
print(sonlar)
yigindi=sum(sonlar)
print(yigindi)
katta=max(sonlar)
kichik=min(sonlar)
print(katta,kichik)
print(max(sonlar)-min(sonlar))
print(max(sonlar)+min(sonlar))
boshson=sonlar[0:10]
print(boshson)
print(sonlar[2:10])
print(sonlar[-10:-1])