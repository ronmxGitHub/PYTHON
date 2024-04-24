#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 1-usul \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 2-usul \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
# talaba1 = Talaba("Alijon","Xujayev",2000)
#
# talaba1.bosqich= 2
# # talaba1.ism="Jahon"
# # print(talaba1.bosqich)
# print(talaba1.get_info())

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 3-usul \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
#
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
#
# talaba1 = Talaba("Alijon","Xujayev",2000)
#
# talaba1.set_bosqich(3)
# print(talaba1.get_info())

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 4-usul \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1    #defolt qiymat
#
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
#
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
#
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1                   #qiymati 1 martadan oshdi 2 qoysa 2tadan oshadi
# talaba1 = Talaba("Alijon","Xujayev",2000)
# print(talaba1.get_info())
#
# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# talaba1.update_bosqich() # 2 bosqichga oshiramiz
# talaba1.update_bosqich() # 3 bosqichga oshiramiz
#
# print(talaba1.get_info())

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 2 ta class qo'shish \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1    #defolt qiymat
#
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
#
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
#
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1
#
#
# class Fan():
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
#
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]   # Talabalar haqida malumot olish
#
# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)
#
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
#
# print(matematika.talabalar_soni)
# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Nuqta yoki metod \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def set_bosqich(self, bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich

    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        """Talabaning yoshini qaytaradi"""
        return yil - self.tyil

talaba1 = Talaba("Alijon","Xujayev",2000)

# print(dir(Talaba))
# print(dir(Fan))
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))
print(talaba1.__dict__)
print(talaba1.__dict__.keys())


