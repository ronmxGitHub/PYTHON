class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.ism)
# print(talaba1.familiya)

    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")
talaba4 = Talaba("Hasan","Akbarov",2004)
talaba4.tanishtir()

# class User:
#     def __int__(self, name, username, email):
#         self.name = name
#         self.uname = username
#         self.mail = email
#
#     def tanishtir(self):
#         print(f"Ismi: {self.name} familya: {self.username} email: {self.email} yilda tu'gilganman")
# talaba = User("alijon1994", "Alijon Valiyev", "alijon1994@gmail.com")
# talaba.tanishtir()
