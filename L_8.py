#\\\\\\\\\\\\1-Chiquvchi javob do'stingizni ismini kiritganda uni sevimli kino-filmlarini chiqarsin.\\\\
filmlar={
    'Ali':['Terminator','Bryusli'],
    'vali':['Shaytanat','Multifilm'],
    'hasan': ['Shum bola', 'Osmondagi bolalar'],
    'husan': ['Tabib', 'Qashqirlar'],
    'maryam': ['Josus', 'Yulduzlar jangi'],
}
dasturchi=input("Do'stingiz ismini kiriting:")
film=""
for key in filmlar:
    if key.lower()==dasturchi.lower():
        film=key
if film:
    print(filmlar[film])
else:
    print("Bu yerda mening do'stim yo'q")


#\\\\\\\\\\\\\\\\\\\\2-Har bir davlat haqida ma'lumotni konsolga chiqaring.\\\\\\\\\\\\\\\\\\\\\\\\\

davlatlar= {
    'angliya':'london',
    'turkiya':'istanbul',
    'turkmaniston':'ashgabat',
    'uzbekiston':'toshkent',
    'belarus':'minsk'
}
# hamkasblar = {
#     'uzbekiston':{'poytaxt':'Toshkent',
#                   'ason': 37,
#                   'vson':12,
#                   'ymaydon':448978,
#                   'viloyatlari':['xorazm','toshkent', 'buxoro', '...']
#                   },
#     'angliya':{'poytaxt':'london',
#                'ason':57,
#                'vson':1995,
#                'ymaydon':132930,
#                'viloyatlari':['sql','C++']
#                },
#     'turkiya':{'poytaxt':'istanbul',
#                'ason': 57,
#                'vson':81,
#                'ymaydon':783562,
#                'viloyatlari':['Ankara','Kırklareli','Bursa', '...']
#                }
#     }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()}, poyataxti: {info['poytaxt'].title()}, "
#           f"Aholisi soni: {info['ason']} mlnga yaqin. "
#           f"Yer maydoni: {info['ymaydon']} km kv \n"
#           f"Viloyatlari: {info['vson']}ta viloyati bor")
#     for viloyat in info['viloyatlari']:
#         print(viloyat.upper())