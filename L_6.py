# yosh=int(input("Yoshingiz nechida?"))
# if yosh>60 or yosh<5:
#     price=0
# elif yosh<18:
#     price=15000
# elif yosh>=18:
#     price=25000
# print(f"Sizga kirish {price} so'm")
#
#
# son1 = float(input("1 : Enter Number : "))
# son2 = float(input("2 : Enter Number : "))
# if son1 == son2:
#     print("Bu sonlar teng ")
# elif son1 > son2:
#     print("Birinchi son katta")
# else:
#     print("Ikkinchi son  Katta")
#
# a=int(input('sonni kiriting'))
# numbers=[]
# for i in range(3, 16):
#     if a % i==0:
#         numbers.append(i)
# print(numbers)

users = ['azamat', 'jumabayev', 'pdp', 'itpark', 'users']
login = input("Yangi login kiriting:")
if login in users:
    print("Yangi login kiriting, bu login band")
else:
    print("Login qabul qilindi")