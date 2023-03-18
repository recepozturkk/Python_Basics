
number = int(input("Lütfen bir sayı giriniz: "))
sayac = 0
for i in range(2,number):
    if (number%i==0):
        sayac = 1
        break

if (sayac == 0):
    print("Girdiğiniz sayı asaldır!")
else:
    print("Girdiğiniz sayı asal değildir!")



