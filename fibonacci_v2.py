# fibonacci sayıları kodu
# 2. versiyon
i = int(input("Fibonacci dizisi sınırını belirleyin: "))
a = 0
b = 1
print(a)
while b < i:    # b sayısını kullanıcıdan aldığımız sayı ile sınırladım.
    print(b)    # döngünün her bir adımında b sayısının son hali ekrana basılıyor.
    b = a + b   # kendinden önceki iki sayının toplamını b ye eşitledim.
    a = b - a   # yeni oluşan b nin kendinden bir önceki sayı eski b
                # eski b yeni oluşan b ye a nın eklenmemiş halidir.
                # bu yüzden yeni b den eski a yı çıkarıp yeni a yı oluşturdum.

# instagram.com/furcanomer