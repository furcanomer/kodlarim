# ikiz asallar sonsuza kadar gidiyor mu?
# bu kanıtlanmış bir şey değil
# bu durumu ölçmek için yazdığım bir program
# bir sayı girersiniz ve program bu sayıdan itibaren
# birer birer ilerler ve ikiz asalları üretir
# ürettiği tüm sayıları da programı çalıştırdığınız
# dizinde bir text dosyasına kaydeder
import os
def asalmi(x):
    if x == 2:
        return 1
    elif x < 2:
        return 0
    else:
        for i in range(2,x):
            if x % i == 0:
                return 0
           
        return 1
print("ikiz_asallar 1.1")
print("https://github.com/furcanomer\n")

while True: 
    dosya_adi = input("oluşturulacak dosya adı ne olsun: ")
    dosyam = dosya_adi+".txt"
    if os.path.isfile(dosyam):
        print("böyle bir dosya var. başka bir dosya adı girin.")
    else:
        dosya = open(dosyam,"a")
        print("Tamamdır. Dosya başarıyla oluşturuldu.")
        break

sayi = int(input("Başlangıç sayısını girin: "))
sayi2 = sayi + 2



while True:
    if asalmi(sayi) and asalmi(sayi2):
        print(sayi,sayi2)
        yazi = (str(sayi)+" "+str(sayi2)+"\n")
        dosya.write(yazi)
    else:
        pass

    sayi += 1
    sayi2 = sayi + 2
