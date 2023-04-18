import os
baslik = "Sayı Tahmin Oyunu 1.0\n"
print(baslik)
print("""Sayıyı aklında tutan kişi, aklında tuttuğu sayıyı programa girer.
Sonra program, akılda tutulan sayıyı kendi zekasında tutar ve ekrandan gizler.
Sonra tahmin etmeye çalışan oyuncu veya oyuncular
ekrana tahmin ettikleri sayıları girerler.
Eğer başarılı olurlarsa oyun biter.
Eğer yanlış tahmin ederlerse oyun, doğru tahmin edilene kadar devam eder.
""")
tutulan_sayi = int(input("Tuttuğun sayıyı gir: "))
os.system("cls")
print(baslik)
while True:
    sayi = int(input("Sayıyı tahmin et: "))
    if (sayi == tutulan_sayi):
        print("Bravo Sayıyı doğru tahmin ettin\n.")
        break
    else:
        continue
a = input("Oyundan çıkmak için 'Enter' tuşuna basabilirsin")
