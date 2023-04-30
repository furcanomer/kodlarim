# ikiz asallar sonsuza kadar gidiyor mu?
# bu kanıtlanmış bir şey değil
# bu durumu ölçmek için yazdığım bir program
# bir sayı girersiniz ve program bu sayıdan itibaren
# birer birer ilerler ve ikiz asalları üretir
# ürettiği tüm sayıları da programı çalıştırdığınız
# dizinde bir text dosyasına kaydeder

def asalmi(x):
    if x == 2:
        return 1
    elif x == 1:
        return 0
    elif x == 0:
        return 0
    elif x < 0:
        return 0
    else:
        for i in range(2,x):
            if x % i == 0:
                return 0
           
        return 1
            
sayi = int(input("Başlangıç sayısını gir: "))
sayi2 = sayi + 2

while True:
    if asalmi(sayi) and asalmi(sayi2):
        print(sayi,sayi2)
        yazi = (str(sayi)+" "+str(sayi2)+"\n")
        dosya = open("ikiz_asallar.txt","a")
        dosya.write(yazi)
    else:
        pass

    sayi += 1
    sayi2 = sayi + 2
