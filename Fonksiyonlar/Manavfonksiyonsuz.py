

print("Manavımıza Hoşgeldiniz.")
meyve = input("Hangi meyveyi almak istersiniz(kilosu 5 TL): ")

if(meyve=="elma"):
    kilo = int(input("Kaç kilo almak istersiniz: "))
    tutar = kilo * 5
    print("Ödemeniz gereken tutar: ", tutar)
elif(meyve=="armut"):
    kilo = int(input("Kaç kilo almak istersiniz: "))
    tutar = kilo * 5
    print("Ödemeniz gereken tutar: ", tutar)
elif(meyve=="portakal"):
    kilo = int(input("Kaç kilo almak istersiniz: "))
    tutar = kilo * 5
    print("Ödemeniz gereken tutar: ", tutar)
else:
    print("İstediğiniz meyve maalesef bulunmamaktadır!")