username = "furcanomer"
password = "1234"

giris = 3

while (giris > 0):
    
    username_2 = input("Kullanıcı adınızı giriniz: ")
    password_2 = input("Şifrenizi giriniz: ")

    if (username == username_2 and password == password_2):
        print("Kullanıcı adınız ve şifreniz doğru.\nSisteme giriş yaptınız.\n")
        break

    else:
        giris -=1
        print("Kullanıcı adınız ve şifreniz yanlış.")
        if(giris > 0):
            print("Kalan hakkınız: " + str(giris) + "\nTekrar deneyiniz.\n")
        continue

if (giris == 0):
    print("3 kere yanlış giriş yaptınız. Hoşçakalın.")