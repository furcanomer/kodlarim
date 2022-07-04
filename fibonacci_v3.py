# fibonacci sayıları kodu
# 3. versiyon
# instagram.com/furcanomer
while True: # programın ana döngüsü
    try:    # Hata kontrolü yaptım. Kullanıcı, sayı girilmesi gereken yere yazı yazabilir.
        i = float(input("Fibonacci dizisi sınırını belirleyin: "))  # istediğimiz sayı tipini gerçek sayı (float) yaptım
                                                                    # ki kullanıcı gerçek sayı da yazabilsin.
                                                                    # programda hata meydana gelmesin.

        if i > 0:
            a = 0
            b = 1
            print(a)
            while b < i:    # b sayısını kullanıcıdan aldığımız sayı ile sınırladım.
                print(b)    # döngünün her bir adımında b sayısının son hali ekrana basılıyor.
                b = a + b   # kendinden önceki iki sayının toplamını b ye eşitledim.
                a = b - a   # yeni oluşan b nin kendinden bir önceki sayı eski b
                            # eski b yeni oluşan b ye a nın eklenmemiş halidir.
                            # bu yüzden yeni b den eski a yı çıkarıp yeni a yı oluşturdum.
            break   # program başarılı bir şekilde çalıştığı için ana while döngüsünü sonlandırıyorum.
    
        elif i <= 0:
            print("Lütfen poztif bir sayı giriniz.")
            continue    # pozitif bir sayı girilmediği için ana while döngüsünü yeniden başlattım.

        else:   # Tanımlanamayan bir sayı girilebilr diye temkinli davrandım.
            print("Tanımlanamayan durum.")
            continue    # Tanımlanamayan bir durum oluştuğu için ana while döngüsünü yeniden başlattım.

    except ValueError:  # Sayı istediğimiz yere yazı yazılabilir diye hata kontrolü yaptım.              
        print("Sayı girilmesi yere yazı yazdınız.\nLütfen sayı giriniz.")   #Bu hatayı kullanıcıya bildirdim.
        continue    # Bir hata meydana geldiği için ana while döngüsünü yeniden başlattım.
