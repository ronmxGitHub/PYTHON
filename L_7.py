# kompyuter = {'model':'samsung', 'rang':'oq'}
# print(kompyuter)
import random

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# kompyuter = {'model':'samsung', 'rang':'oq'}
# komp=kompyuter.get('model')
# print(komp)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# komp_qurilmalri={
#     'printer':15000,
#     'skaner':10000,
#     'kalonka':5000,
#     'kamera':8000,
# }
# print(komp_qurilmalri.keys())

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# davlatlar= {
#     'angliya':'london',
#     'turkiya':'istanbul',
#     'turkmaniston':'ashgabat',
#     'uzbekiston':'toshkent',
#     'belarus':'minsk'
# }
# print('Davlatlar:')
# for davlat in davlatlar.keys():
#     print(davlat.title())

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# davlatlar= {
#     'angliya:':'london',
#     'turkiya':'istanbul',
#     'turkmaniston':'ashgabat',
#     'uzbekiston':'toshkent',
#     'belarus':'minsk'
# }
# mamlakat=['angliya:', 'turkiya', 'turkmaniston','uzbekiston', 'belarus']
# for davlat in sorted(davlatlar):
#     if davlat in mamlakat:
#         print(f"{davlat.title()} {davlatlar[davlat]}")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# davlatlar= {
#     'angliya':'london',
#     'turkiya':'istanbul',
#     'turkmaniston':'ashgabat',
#     'uzbekiston':'toshkent',
#     'belarus':'minsk'
# }
# for davlat, poytaxt in davlatlar.items():
#     print(f"Davlat: {davlat.title()}")
#     print(f"Poytaxt: {poytaxt.title()} \n")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# davlatlar= {
#     'angliya':'london',
#     'turkiya':'istanbul',
#     'turkmaniston':'ashgabat',
#     'uzbekiston':'toshkent',
#     'belarus':'minsk'
# }
# ks = davlatlar.keys()
# keylist=list(ks)
# rn = random.randrange(0, len(keylist))
# question=keylist[rn]
# print(question,'ning poytaxti ?')
# davlat=input("Davlat kiriting:")
# if davlat.lower()==davlatlar[question].lower():
#     print('Yaxshi')
# else:
#     print("Yo'q adashdingiz")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\