pi = 3.14

def kare_cevre(kare_kenar):
    cevre = kare_kenar*4
    print("Karenin çevresi: ", cevre)
def kare_alan(kare_kenar):
    alan = kare_kenar**2
    print("Karenin alanı: ", alan)
def dikdortgen_cevre(kisa_kenar, uzun_kenar):
    cevre = (kisa_kenar+uzun_kenar)*2
    print("Dikdörtgenin çevresi: ", cevre)
def dikdortgen_alan(kisa_kenar, uzun_kenar):
    alan = kisa_kenar*uzun_kenar
    print("Dikdörtgenin alanı: ", alan)
def ucgen_cevre(taban, ilk_kenar, ikinci_kenar):
    cevre = taban + ilk_kenar + ikinci_kenar
    print("Üçgenin çevresi: ", cevre)
def ucgen_alan(taban, yukseklik):
    alan = (taban * yukseklik) / 2
    print("Üçgenin alanı: ", alan)
def daire_cevre(yari_cap):
    cevre = 2 * pi * yari_cap
    print("Dairenin çevresi: ", cevre)
def daire_alan(yari_cap):
    alan = pi * yari_cap**2
    print("Dairenin alanı: ", alan)
def hesaplama_turleri():
    print("""İstediğiniz hesaplama türü için rakam giriniz
                1- Çevre
                2- Alan""")
def hata_mesaji():
    print("**********Eksik ya da hatalı tuşlama!**********")
while True:
    print("""Şekil Çevre-Alan hesaplama aracına hoşgeldiniz.
    Hesaplama yapılabilen şekiller:
    Kare
    Dikdörtgen
    Üçgen
    Daire

    Programdan çıkmak için 'q' tuşlayınız!""")
    sekil = input("Lütfen şekil seçiniz: ")
    if(sekil=="q"):
        print("Program kapatılıyor...")
        break
    elif(sekil == "kare" or sekil=="Kare"):
        while True:
            hesaplama_turleri()
            hesaplama_turu = int(input("Lütfen hesaplama türünü seçiniz: "))
            if (hesaplama_turu==1):
                kare_kenar = int(input("Lütfen karenin kenarını giriniz: "))
                kare_cevre(kare_kenar)
                break
            elif(hesaplama_turu==2):
                kare_kenar = int(input("Lütfen karenin kenarını giriniz: "))
                kare_alan(kare_kenar)
                break
            else:
                hata_mesaji()
    elif(sekil=="dikdörtgen" or sekil=="Dikdörtgen"):
        while True:
            hesaplama_turleri()
            hesaplama_turu = int(input("Lütfen hesaplama türünü seçiniz: "))
            if (hesaplama_turu == 1):
                kisa_kenar = int(input("Lütfen kısa kenarı giriniz: "))
                uzun_kenar = int(input("Lütfen uzun kenarı giriniz: "))
                dikdortgen_cevre(kisa_kenar, uzun_kenar)
                break
            elif(hesaplama_turu==2):
                kisa_kenar = int(input("Lütfen kısa kenarı giriniz: "))
                uzun_kenar = int(input("Lütfen uzun kenarı giriniz: "))
                dikdortgen_alan(uzun_kenar, kisa_kenar)
                break
            else:
                hata_mesaji()
    elif(sekil=="Üçgen" or sekil=="üçgen"):
        while True:
            hesaplama_turleri()
            hesaplama_turu = int(input("Lütfen hesaplama türünü seçiniz: "))
            if (hesaplama_turu == 1):
                taban = int(input("Lütfen taban uzunluğunu giriniz: "))
                ilk_kenar = int(input("Lütfen ilk kenarı giriniz: "))
                ikinci_kenar = int(input("Lütfen ikinci kenarı giriniz: "))
                ucgen_cevre(taban, ilk_kenar, ikinci_kenar)
                break
            elif(hesaplama_turu==2):
                taban = int(input("Lütfen taban uzunluğunu giriniz: "))
                ilk_kenar = int(input("Lütfen ilk kenarı giriniz: "))
                ucgen_alan(taban, ilk_kenar)
                break
            else:
                hata_mesaji()
    elif(sekil=="Daire" or sekil=="daire"):
        while True:
            hesaplama_turleri()
            hesaplama_turu = int(input("Lütfen hesaplama türünü seçiniz: "))
            if (hesaplama_turu == 1):
                yari_cap = int(input("Lütfen dairenin yarıçapını girin: "))
                daire_cevre(yari_cap)
                break
            elif (hesaplama_turu == 2):
                yari_cap = int(input("Lütfen dairenin yarıçapını girin: "))
                daire_alan(yari_cap)
                break
            else:
                hata_mesaji()
    else:
        hata_mesaji()












