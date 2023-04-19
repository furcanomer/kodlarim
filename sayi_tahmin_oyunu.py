import os
baslik = "Sayı Tahmin Oyunu 2.0\n"
print(baslik)
print("""Sayıyı aklında tutan kişi, aklında tuttuğu sayıyının, hangi sayılar aralığında olduğunu
belirtir. Sonra aklında tuttuğu sayıyı programa girer.
Sonra program, akılda tutulan sayıyı kendi zekasında tutar ve ekrandan gizler.
Sonra sayıyı tahmin etmeye çalışan oyuncu veya oyuncular
ekrana tahmin ettikleri sayıları girerler.
Eğer başarılı olurlarsa oyun biter.
Eğer yanlış tahmin ederlerse oyun, doğru tahmin edilene kadar devam eder.
""")
bas = int(input("Tuttuğun sayı, hangi sayılar arasında?\nAralığın ilk değeri: "))
bit = int(input("Aralığın son son değeri: "))
while True: 
    tutulan_sayi = int(input("Tuttuğun sayıyı gir: "))
    if tutulan_sayi >= bas and tutulan_sayi <= bit:
        os.system("cls")
        print(baslik)
        print("Tahmin edeceğin sayı,",bas,"ve",bit,"aralığında olmalıdır.")
        while True:
            sayi = int(input("Sayıyı tahmin et: "))
            if (sayi == tutulan_sayi):
                print("Bravo Sayıyı doğru tahmin ettin.\n")
                break
            elif sayi < bas or sayi > bit:
                print("Tahmin ettiğin sayı,",bas,"ve",bit,"aralığında değil.\nTekrar dene.")
                continue
            else:
                print("Yanlış tahmin. Tekrar dene.")
                continue
    else:
        print("Tuttuğun sayı,",bas,"ve",bit,"aralığında değil.\nTahmin ettiğin sayıyı tekrar gir.")
        continue
    break
a = input("Oyundan çıkmak için 'Enter' tuşuna basabilirsin\n")
