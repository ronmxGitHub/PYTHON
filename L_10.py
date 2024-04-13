#Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz
#bo'linuvchi, 1 dan katta musbat sonlar)
# def tub_sonlar(n, m):
#     tub = []
#     while n <= m:
#         i = n
#         j = 1
#         boluvchi = 0
#         while j <= i:
#             if i % j == 0:
#                 boluvchi += 1
#             j += 1
#         if boluvchi == 2:
#             tub.append(i)
#         n += 1
#     return tub
# n = int(input("n="))
# m = int(input("m="))
# print(tub_sonlar(n,m))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#(Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi
#funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik
#Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.)

# def fibonachi(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1] + sonlar[x-2])
#     return sonlar
# print(fibonachi(100))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at
#ko'rinishida qaytaruvchi funksiya yozing

def aylana_hisobla(radius):
    diameter = 2*radius
    perimeter = 2*3.14*radius
    javob = {
    'diameter':diameter,
    'perimeter':perimeter,
    'yuza':None
    }
    return javob
n = float(input("Aylana radiusini kiriting: "))
aylana_malumotlari = aylana_hisobla(n)
print(aylana_malumotlari)