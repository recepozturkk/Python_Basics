

print("Faktöriyel hesaplama programına hoş geldiniz.")

number = int(input("Lütfen hesaplamak istediğiniz sayıyı giriniz: "))

faktöriyel = 1
for i in range(2,number+1):
    faktöriyel *= i
    print("i değeri: ",i)
    print("faktöriyel değeri: ",faktöriyel)
print("Sayının faktöriyeli: ",faktöriyel)