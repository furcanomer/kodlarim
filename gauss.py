def gauss(n):
    return int((n*(n+1))/2)

print("Gauss 1.0\n")

while(True):
    sayi = int(input("Sayı Giriniz: "))
    sonuc = gauss(sayi)
    print("1'den "+str(sayi)+" sayısına kadar olan sayıların toplamı: "+str(sonuc)+"\n")
