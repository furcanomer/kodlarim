import os
while True:
    os.system("cls")
    baslik = "Sayı Tahmin Oyunu 2.2.1\n"
    print(baslik)
    print("""Sayıyı aklında tutan kişi, aklında tuttuğu sayıyının, hangi sayılar aralığında olduğunu
belirtir. Sonra aklında tuttuğu sayıyı programa girer.
Sonra program, akılda tutulan sayıyı kendi zekasında tutar ve ekrandan gizler.
Sonra sayıyı tahmin etmeye çalışan oyuncu veya oyuncular
ekrana tahmin ettikleri sayıları girerler.
Eğer başarılı olurlarsa oyun biter.
Eğer yanlış tahmin ederlerse oyun, doğru tahmin edilene kadar devam eder.
""")
    while True:
        x = int(input("Tuttuğun sayı, hangi sayılar arasında?\nAralığın ilk değeri: "))
        y = int(input("Aralığın son son değeri: "))

        if (x > y):
            bas = y
            bit = x
            break
        elif (x < y):
            bas = x
            bit = y
            break
        else:
            print("Aralık belirtirken, başlangıç sayısı ve bitiş sayısı eşit olamaz.\nTekrar dene.")
            continue
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
            print("Tuttuğun sayı,",bas,"ve",bit,"aralığında değil.\nTuttuğun sayıyı tekrar gir.")
            continue
        break
    cikis = 0
    while True:
        a = input("Oyun bitti. Tekrar oynamak ister misin? (E) evet / (H) hayır\n--> ")
        if (a == "H" or a =="h"):
            cikis = 1; break
        elif (a == "e" or a == "E"):
            break
        else:
            print("Anlamadım. Tekrar söyle.")
            continue
    if (cikis == 1):
        break
    else:
        continue
