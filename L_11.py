#\\\\\\\\Arifmetik amalni bajaruvchi funksiya (1-usul)////////////
# def arfimetik_amal(amal,*sonlar):
#     amal1='+'
#     amal2='-'
#     amal3='/'
#     amal4='*'
#
#     if amal==amal1:
#         return sum(sonlar)
#     elif amal==amal2:
#         return sonlar[0]-(sum(sonlar)-sonlar[0])
#     elif amal==amal3:
#         natija=sonlar[0]
#         for i in sonlar:
#             natija=natija/i
#         return natija
#     elif amal==amal4:
#         natija=1
#         for i in sonlar:
#             natija*=i
#         return natija
#
# result=arfimetik_amal("*",6,7,8,9)
# print(result)

#\\\\\\\\Arifmetik amalni bajaruvchi funksiya (2-usul)////////////

def amal(belgi,*numbers):
    kop = 1
    ayirma = numbers[0]
    bolinma = numbers[0]
    if belgi == '+':
        return sum(numbers)
    elif belgi == '*':
        for n in numbers:
            kop *= n
        return kop
    elif belgi == '-':
        for n in numbers:
            ayirma -= n
        return ayirma + numbers[0]
    elif belgi == '/':
        for n in numbers:
            bolinma /= n
        return bolinma * numbers[0]
    else:
        result = "Iltimos! quyidagi belgilardan bittasini tanlang:('+','-','*','/')"
        return result

belgi = input("('+', '-', '*', '/') shulardan bittasini tanlang!:")
print(amal(belgi,4,5,8))

# def birlashtir(*args):
#     birlashgan_royxat = []
#     for royxat in args:
#         birlashgan_royxat.extend(royxat)
#     return birlashgan_royxat
# royxat1 = [1,2,3]
# royxat2 = [4,5,6]
# royxat3 = [7,8,9]
# birlashgan = birlashtir(royxat1,royxat2,royxat3)
# print(birlashgan)
#
# lits = [*royxat1, *royxat2, *royxat3]
# print(lits)