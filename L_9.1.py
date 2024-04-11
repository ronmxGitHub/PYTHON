# def tub_sonlarni_tekshir():
#     n=input('son kirit: ')
#     print('Bu tub son' if len([i for i in range(1, int(n)+1) if int(n) %i == 0]) == 2 else 'Bu son tub emas')
# tub_sonlarni_tekshir()


def ekubni_top(a,b):
    while a!= b:
        if a>b:
            a-=b
        else:
            b-=a
    print(f"Ekub {a}")
ekubni_top(15,40)