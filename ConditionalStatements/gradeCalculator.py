again = 0
while(again==0):
    print("""Not hesaplama aracına göre harf notu olarak puan tablosu:
    AA  90-100
    BA  85-89
    BB  80-84
    CB  75-79
    CC  70-74
    DC  65-69
    DD  60-64
    FD  50-59
    FF  0-49""")
    firstvisa = int(input("Lütfen ilk vize sonucunu giriniz: "))
    secondvisa = int(input("Lütfen ikinci vize sonucunu giriniz: "))
    finalgrade = int(input("Lütfen final notunuzu giriniz: "))
    averaGrade = firstvisa*0.3 + secondvisa*0.3 + finalgrade*0.4


    if(averaGrade >= 90 ):
        print("Notunuz: ", averaGrade, "AA")
    elif(averaGrade >= 85):
        print("Notunuz: ", averaGrade, "BA")
    elif(averaGrade >= 80):
        print("Notunuz: ", averaGrade, "BB")
    elif(averaGrade >= 75):
        print("Notunuz: ", averaGrade, "CB")
    elif(averaGrade >= 70):
        print("Notunuz: ", averaGrade, "CC")
    elif(averaGrade >= 65):
        print("Notunuz: ", averaGrade, "DC")
    elif(averaGrade >= 60):
        print("Notunuz: ", averaGrade, "DD")
    elif(averaGrade >= 50):
        print("Notunuz: ", averaGrade, "FD")
    else:
        print("Notunuz: ", averaGrade, "FF")
