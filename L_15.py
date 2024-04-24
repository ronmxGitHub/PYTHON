# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
#
#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil
#
# # inson = Shaxs("Hasan","Alimov","FB001122",1995)
# # print(f"{inson.get_info()}. {inson.get_age(2024)} yoshda.")
#
# # class Talaba(Shaxs):
# #     """Talaba klassi"""
# #     def __init__(self, ism, familiya, passport, tyil):
# #         """Talabaning xususiyatlari"""
# #         super().__init__(ism, familiya, passport, tyil)
# # talaba = Talaba("Valijon", "Aliyev", "FA112299", 2000)
# # print(talaba.get_info())
# # print(talaba.get_age(2024))
#
# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
#
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
#
# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")
# print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")
# print(f"{talaba.get_bosqich()}-bosqich talabasi")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Obyekt ichida obyekt/////////////////////////

# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
#
#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil
#
# class Manzil:
#     """Manzil saqlash uchun klass"""
#
#     def __init__(self, uy, kocha, tuman, viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
#
#     def get_manzil(self):
#         """Manzilni ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil
#
# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
#
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
#
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
#
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
#
# talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Xorazm")
# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)
# print(talaba.manzil.get_manzil())
# print(talaba.manzil.tuman)

#\\\\\\\\\\\\\\\\\\\Inkapsulatsiya////////////////////////////////

# from uuid import uuid4


# class Avto:
#     """Avtomobil klassi"""
#
#     def __init__(self, make, model, rang, yil, narh, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#
#     def get_km(self):
#         return self.__km
#
#     def get_id(self):
#         return self.__id
#
#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")
#
#
# avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# # avto1.__km
# print(f"ID: {avto1.get_id()}")
# avto1.add_km(1500)
# print(f"Km: {avto1.get_km()}")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# from uuid import uuid4
#
# class Avto:
#     """Avtomobil klassi"""
#     num_avto = 0
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.num_avto += 1
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# print(avto1.num_avto)

class Avto:
    """Avtomobil klassi"""
    __num_avto = 0 # klassga oid xususiyat
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
print(Avto.get_num_avto())
