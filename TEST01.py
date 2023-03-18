print("Lütfen aşağıdaki işlemlerden birini seçerek enter a basınız.")

print("""Toplama = +
Çıkarma = -
Çarpma = *
Bölme = /""")
islem = input("Lütfen yapmak istediğiniz işleme ait sembölü girip enter a basınız: ")
if(islem == "+"):
    a = int(input("Lütfen ilk sayıyı giriniz: "))
    b = int(input("Lütfen ikinci sayıyı giriniz: "))
    print("Sonuç: ", a+b)
elif(islem == "-"):
    a = int(input("Lütfen ilk sayıyı giriniz: "))
    b = int(input("Lütfen ikinci sayıyı giriniz: "))
    print("Sonuç: ", a - b)
elif(islem == "*"):
    a = int(input("Lütfen ilk sayıyı giriniz: "))
    b = int(input("Lütfen ikinci sayıyı giriniz: "))
    print("Sonuç: ", a * b)
elif(islem == "/"):
    a = int(input("Lütfen ilk sayıyı giriniz: "))
    b = int(input("Lütfen ikinci sayıyı giriniz: "))
    print("Sonuç: ", a / b)
else:
    print("Lütfen belirtilen işlemlerden birini seçin:")





