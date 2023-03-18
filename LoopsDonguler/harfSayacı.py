
text = """Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır 
metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat 
numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı 
1500'lerden beri endüstri standardı sahte metinler olarak kullanılmıştır. 
Beşyüz yıl boyunca varlığını sürdürmekle kalmamış, aynı zamanda pek değişmeden 
elektronik dizgiye de sıçramıştır. 1960'larda Lorem Ipsum pasajları da içeren 
Letraset yapraklarının yayınlanması ile ve yakın zamanda Aldus PageMaker gibi 
Lorem Ipsum sürümleri içeren masaüstü yayıncılık yazılımları ile popüler olmuştur."""

letter = input("Metin içinde hangi harfin kaç kez tekrar edildiğini öğrenmek için lütfen harfi yazınız: ")
repeat = 0
for i in text:
    if(i == letter):

        repeat += 1

print("Belirttiğiniz harf metinde ",repeat,"kez tekrar edilmiştir.")

