import math

newArray = [1,2,2,3,3,3,5,7,11,15]


# def factorial(index):
#     carpim = 1
#     if(index != 0):
#         for deger in index:
#             carpim = carpim*deger
#     print(carpim)
#     return carpim

def faktoriyel(n):

    faktoriyel = 1

    for i in range(n):
        faktoriyel *= i + 1
    return faktoriyel
print(faktoriyel(5))



