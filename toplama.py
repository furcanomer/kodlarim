while True:

    while True:
        try:    
            sayi1 = int(input("1. sayı: "))
            break
        except:
            print("Yanlış şeyler girdiniz.")
            continue 
        
    while True:
        try:
            sayi2 = int(input("2. sayı: "))
            break
        except:
            print("Yanlış şeyler girdiniz.")
            continue
            
                    
    toplam = sayi1 + sayi2

    print(toplam)