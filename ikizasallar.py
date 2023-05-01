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
print(" * * *  ikiz Asallar 1.3  * * * ")
print("-----------------------------------")
print("https://github.com/furcanomer")
print("-----------------------------------\n")
print("-----------------------------------------------------------------------")
print("Uyarı 1:     Programı kapatırken Ctrl+c tuş kombinasyonuyla kapatın.")
print("             Penceredeki çarpı tuşuyla kapatırsanız")
print("             üretilen sayılar text dosyasına kaydolmaz.\n")
print("Uyarı 2:     Büyük bir sayı girerseniz program yavaş çalışacaktır.")
print("-----------------------------------------------------------------------\n")

while True: 
    dosya_adi = input("Oluşturulacak dosya adı ne olsun: ")
    dosyam = dosya_adi+".txt"
    if os.path.isfile(dosyam):
        print("Böyle bir dosya var. Başka bir dosya adı girin.")
    else:
        dosya = open(dosyam,"a")
        print("Tamamdır. Dosya başarıyla oluşturuldu.\n")
        break
hata = 0
while True:
    try:
        sayi = int(input("Başlangıç sayısını girin: "))
    except:
        hata = 1
    
    if (hata == 1):
        print("Lütfen doğal sayı girin!\n")
        hata = 0
        continue
    elif (sayi < 0):
        print("Negatif sayılar asal olamaz!\nLütfen doğal sayı girin.\n")
        continue
    else:
        break

sayi2 = sayi + 2
print("\n")

while True:
    if asalmi(sayi) and asalmi(sayi2):
        print(sayi,sayi2)
        yazi = (str(sayi)+" "+str(sayi2)+"\n")
        dosya.write(yazi)
    else:
        pass

    sayi += 1
    sayi2 = sayi + 2
