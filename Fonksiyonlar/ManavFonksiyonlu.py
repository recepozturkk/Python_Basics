
print("Manavımıza Hoşgeldiniz.")

def muhasebe():
    kilo = int(input("Kaç kilo almak istersiniz: "))
    tutar = kilo * 5
    print("Ödemeniz gereken tutar: ", tutar)

meyve = input("Hangi meyveyi almak istersiniz(kilosu 5 TL): ")

if(meyve=="elma"):
    muhasebe()
elif(meyve=="armut"):
    muhasebe()
elif(meyve=="portakal"):
    muhasebe()
else:
    print("İstediğiniz meyve maalesef bulunmamaktadır!")