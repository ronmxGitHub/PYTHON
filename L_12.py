sonlar = list(range(-1,10))
son = list(filter(lambda x : x % 2 == 0,sonlar))
print(son)
kvadrat = list(map(lambda x : x * x, son))
print(kvadrat)

# numbers = list(range(-5,5))
# print(numbers)
# musbat_numbers = list(filter(lambda num: num > 0,numbers))
# print(musbat_numbers)

numbers = list(range(1,6))
teskari_list = lambda num : num[::-1]
print(teskari_list(numbers))