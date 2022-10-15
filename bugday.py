"""
Bir hikaye vardır. Eski zamanlarda bir uyanık, kraldan bugday alma hakkı kazanmış.
Bu uyanık, krala demiş ki "Satranç tahtasının ilk karesine bir buğday koyacağım.
Her bir karede bugday 2 katına çıkarak ilerleyecek ve işin sonunda Ben bu satranç tahtasının
üzerindeki bütün bugdayı alacağım." demiş. Kral, herhalde az gelecek, diye düşünerek
bunu kabul etmiş ama oluşan sonuç baya büyükmüş. işte bu sonucu veren programın kodları.

"""
toplam = 0
bugday = 1
adim = 1
sartancTahtasi = 64

while (adim < sartancTahtasi):
    print(str(adim)+". adım:",bugday)
    adim += 1
    bugday *= 2
    toplam += bugday
    
print(str(adim)+". adım:",bugday)

print("\nToplam:",toplam + 1)
# +1 ilk baştaki bugday değeri işlenmediği için ekledim.
# Toplam değerine ilk adımda 3 eklenmesi gerekirken 2 eklendiği için o ayarı yaptım.
