
def odaCevresi(x,y):
    return (x+y)*2

kisa_kenar1 = int(input("Lütfen kısa kenarı giriniz:"))
uzun_kenar1 = int(input("Lütfen uzun kenarı giriniz:"))

kisa_kenar2 = int(input("Lütfen kısa kenarı giriniz:"))
uzun_kenar2 = int(input("Lütfen uzun kenarı giriniz:"))

oda1 = odaCevresi(kisa_kenar1,uzun_kenar1)
oda2 = odaCevresi(kisa_kenar1,uzun_kenar1)

print("Evinizin çevresi:", oda1+oda2)
